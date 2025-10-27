# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 10:09:11

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 199
- **总 Thread 数**: 30
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 12 threads (135 邮件)
- **RFC**: 3 threads (48 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 14 threads (14 邮件)

---

## 📌 PATCH

共 12 个 thread

---

### Thread 1: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 43 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 26 Apr 2025 13:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的细粒度陷阱（Fine Grained Trap，FGT）处理的改进，特别是引入了 FEAT_FGT2 特性。

1. **原始 Patch/问题内容**：
   该系列补丁（[PATCH v3 00/42]）旨在重构 KVM 的细粒度陷阱处理，增加对 FEAT_FGT2 的支持，并优化现有的 FGT 处理逻辑。补丁数量达 42 个，涉及对多项寄存器的更新和新特性的引入。

2. **之前讨论要点**：
   在之前的讨论中，Marc Zyngier 提到需要对 FGT 处理进行重构，以提高代码的可维护性和可读性，并且强调了对新特性（如 FEAT_FGT2）的支持是紧迫的。补丁中还涉及到对现有 FGT 逻辑的简化和清理。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的具体实现上，包括：
   - 增加了对 FEAT_FGT2 寄存器的描述和处理逻辑。
   - 引入了新的 FGT 措施以确保 KVM 在处理细粒度陷阱时的正确性。
   - 进行了大量的代码重构，以便使用表驱动的方式来配置 FGT。
   - 讨论了如何在 KVM 中实现对新寄存器的上下文切换，并确保主机配置不会泄漏到客户机中。
   - 最终，邮件中提到的补丁将有助于提升 KVM 对新特性的支持，同时保持代码的整洁性和可读性。

总的来说，这一系列补丁标志着 KVM 在 arm64 架构下细粒度陷阱处理能力的显著提升，尤其是对新特性 FEAT_FGT2 的支持。

#### 📝 邮件列表

1. **[04-26 13:27]** [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-26 13:27]** [PATCH v3 01/42] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64 encoding for FEAT_LS64WB
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-26 13:27]** [PATCH v3 02/42] arm64: sysreg: Update ID_AA64MMFR4_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-26 13:27]** [PATCH v3 03/42] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-26 13:27]** [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-26 13:27]** [PATCH v3 05/42] arm64: sysreg: Update ID_AA64PFR0_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-26 13:28]** [PATCH v3 06/42] arm64: sysreg: Update PMSIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-26 13:28]** [PATCH v3 07/42] arm64: sysreg: Update TRBIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-26 13:28]** [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-26 13:28]** [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-26 13:28]** [PATCH v3 10/42] arm64: sysreg: Add system instructions trapped by HFGIRT2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-26 13:28]** [PATCH v3 11/42] arm64: Remove duplicated sysreg encodings
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-26 13:28]** [PATCH v3 12/42] arm64: tools: Resync sysreg.h
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-26 13:28]** [PATCH v3 13/42] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-26 13:28]** [PATCH v3 14/42] arm64: Add FEAT_FGT2 capability
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-26 13:28]** [PATCH v3 15/42] KVM: arm64: Tighten handling of unknown FGT groups
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-26 13:28]** [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[04-26 13:28]** [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[04-26 13:28]** [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_ST64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[04-26 13:28]** [PATCH v3 19/42] KVM: arm64: Don't treat HCRX_EL2 as a FGT register
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[04-26 13:28]** [PATCH v3 20/42] KVM: arm64: Plug FEAT_GCS handling
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[04-26 13:28]** [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[04-26 13:28]** [PATCH v3 22/42] KVM: arm64: Add description of FGT bits leading to EC!=0x18
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[04-26 13:28]** [PATCH v3 23/42] KVM: arm64: Use computed masks as sanitisers for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[04-26 13:28]** [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[04-26 13:28]** [PATCH v3 25/42] KVM: arm64: Propagate FGT masks to the nVHE hypervisor
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[04-26 13:28]** [PATCH v3 26/42] KVM: arm64: Use computed FGT masks to setup FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[04-26 13:28]** [PATCH v3 27/42] KVM: arm64: Remove hand-crafted masks for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[04-26 13:28]** [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[04-26 13:28]** [PATCH v3 29/42] KVM: arm64: Handle PSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[04-26 13:28]** [PATCH v3 30/42] KVM: arm64: Switch to table-driven FGU configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[04-26 13:28]** [PATCH v3 31/42] KVM: arm64: Validate FGT register descriptions against RES0 masks
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[04-26 13:28]** [PATCH v3 32/42] KVM: arm64: Use FGT feature maps to drive RES0 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[04-26 13:28]** [PATCH v3 33/42] KVM: arm64: Allow kvm_has_feat() to take variable arguments
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[04-26 13:28]** [PATCH v3 34/42] KVM: arm64: Use HCRX_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[04-26 13:28]** [PATCH v3 35/42] KVM: arm64: Use HCR_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[04-26 13:28]** [PATCH v3 36/42] KVM: arm64: Add FEAT_FGT2 registers to the VNCR page
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[04-26 13:28]** [PATCH v3 37/42] KVM: arm64: Add sanitisation for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[04-26 13:28]** [PATCH v3 38/42] KVM: arm64: Add trap routing for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[04-26 13:28]** [PATCH v3 39/42] KVM: arm64: Add context-switch for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[04-26 13:28]** [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[04-26 13:28]** [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[04-26 13:28]** [PATCH v3 42/42] KVM: arm64: Handle TSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 0/6] Add FIELD_MODIFY() helper

**📧 邮件数**: 29 | **👥 参与者**: 8 | **📅 开始时间**: Thu, 17 Apr 2025 18:47:07 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是添加 `FIELD_MODIFY()` 辅助宏，该宏属于 `FIELD_XXX` 位域宏系列，旨在提供更好的编译时类型检查，以替代现有的 `xxx_replace_bits()` 函数。历史讨论中，Luo Jie 提出了这一补丁系列，并解释了 `FIELD_MODIFY()` 的功能和必要性，强调了其在内核代码中的应用和对开发者的帮助。

在之前的讨论中，Marc Zyngier 和其他参与者对引入新宏的必要性提出了质疑，认为现有的 `_replace_bits()` 函数已经足够，且缺乏文档支持的问题需要解决。Andrew Lunn 则支持引入 `FIELD_MODIFY()`，认为其提供了更好的可读性和类型安全。

本周的新讨论中，参与者对补丁进行了细节上的审查和修改建议。Markus Elfring 提出了对 Coccinelle 脚本的改进建议，并讨论了支持其他操作模式的可能性。Luo Jie 表示将根据反馈更新补丁。Yury Norov 和 Russell King 继续探讨 `FIELD_MODIFY()` 与 `_replace_bits()` 的区别，尤其是在类型安全和性能方面的影响，强调了在特定情况下使用固定类型的重要性。

总体来看，`FIELD_MODIFY()` 的引入得到了逐步认可，参与者对其在内核开发中的应用表示积极态度，同时也关注到现有工具和文档的完善。

#### 📝 邮件列表

1. **[04-17 18:47]** [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[04-17 18:47]** [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[04-17 18:47]** [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[04-17 18:47]** [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
5. **[04-17 18:47]** [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
6. **[04-17 12:10]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-17 12:23]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-17 19:22]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Andrew Lunn <andrew@lunn.ch>
9. **[04-17 18:45]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-17 19:11]** Re: [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
11. **[04-18 11:08]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
12. **[04-18 11:14]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
13. **[04-18 16:35]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-18 13:04]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
15. **[04-18 13:11]** Re: [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
16. **[04-23 13:01]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
17. **[04-23 21:04]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
18. **[04-23 21:05]** Re: [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
19. **[04-23 21:15]** Re: [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
20. **[04-23 21:19]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
21. **[04-23 18:35]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
22. **[04-23 16:54]** RE: [cocci] [PATCH v3 3/6] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Keller, Jacob E <jacob.e.keller@intel.com>
23. **[04-23 18:44]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
24. **[04-23 18:48]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
25. **[04-23 14:27]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
26. **[04-23 14:44]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
27. **[04-23 20:11]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
28. **[04-23 15:40]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
29. **[04-24 15:24]** RE: [cocci] [PATCH v3 3/6] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Keller, Jacob E <jacob.e.keller@intel.com>

---

### Thread 3: [PATCH v3 00/17] KVM: arm64: Recursive NV support

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:14:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构上实现递归 NV（Nested Virtualization）支持的补丁（PATCH v3 00/17）。该补丁的核心在于对 VNCR_EL2（Virtual Nested Context Register）进行虚拟化管理，允许在嵌套虚拟化环境中更好地处理系统寄存器的访问。

历史讨论中，Marc Zyngier 提到，递归 NV 支持的实现涉及到复杂的上下文切换和内存映射管理，特别是 VNCR 页的管理。补丁系列的目标是确保在不同的虚拟化层次中，能够正确管理 TLB（Translation Lookaside Buffer）和内存映射。

本周的新讨论中，Marc Zyngier 提交了多个补丁，涵盖了 VNCR_EL2 的布局、页面分配、地址转换辅助函数、TLB 无效化机制等多个方面。具体进展包括：
1. **VNCR_EL2 布局添加**：补丁中定义了 VNCR_EL2 的完整布局，以便于后续的虚拟化实现。
2. **页面分配**：在运行 NV 客户机时，分配额外的页面用于系统寄存器访问。
3. **地址转换**：引入了新的地址转换辅助函数，以支持 VNCR_EL2 的虚拟化。
4. **TLB 管理**：补丁中还实现了对 TLB 的管理，确保在不同的虚拟化层次中能够正确处理 TLB 无效化请求。

此外，补丁还增加了对用户空间的支持，允许用户请求 KVM_ARM_VCPU_EL2 功能，标志着该功能的逐步完善。整体来看，这些补丁为 KVM 在 ARM64 上的递归虚拟化提供了重要的支持，尽管仍存在一些未解决的错误和优化空间。

#### 📝 邮件列表

1. **[04-23 16:14]** [PATCH v3 00/17] KVM: arm64: Recursive NV support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-23 16:14]** [PATCH v3 01/17] arm64: sysreg: Add layout for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-23 16:14]** [PATCH v3 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-23 16:14]** [PATCH v3 03/17] KVM: arm64: nv: Extract translation helper from the AT code
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-23 16:14]** [PATCH v3 04/17] KVM: arm64: nv: Snapshot S1 ASID tagging information during walk
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-23 16:14]** [PATCH v3 05/17] KVM: arm64: nv: Move TLBI range decoding to a helper
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-23 16:14]** [PATCH v3 06/17] KVM: arm64: nv: Don't adjust PSTATE.M when L2 is nesting
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-23 16:14]** [PATCH v3 07/17] KVM: arm64: nv: Add pseudo-TLB backing VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-23 16:14]** [PATCH v3 08/17] KVM: arm64: nv: Add userspace and guest handling of VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-23 16:15]** [PATCH v3 09/17] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-23 16:15]** [PATCH v3 10/17] KVM: arm64: nv: Handle mapping of VNCR_EL2 at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-23 16:15]** [PATCH v3 11/17] KVM: arm64: nv: Handle VNCR_EL2 invalidation from MMU notifiers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-23 16:15]** [PATCH v3 12/17] KVM: arm64: nv: Program host's VNCR_EL2 to the fixmap address
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-23 16:15]** [PATCH v3 13/17] KVM: arm64: nv: Add S1 TLB invalidation primitive for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-23 16:15]** [PATCH v3 14/17] KVM: arm64: nv: Plumb TLBI S1E2 into system instruction dispatch
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-23 16:15]** [PATCH v3 15/17] KVM: arm64: nv: Remove dead code from ERET handling
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-23 16:15]** [PATCH v3 16/17] KVM: arm64: Allow userspace to request KVM_ARM_VCPU_EL2*
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[04-23 16:15]** [PATCH v3 17/17] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 16 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 7 Apr 2025 08:20:09 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下，允许使用 VMA（虚拟内存区域）标志进行可缓存的二级映射的补丁（PATCH v3 1/1）。该补丁旨在解决当前 KVM 在处理物理页表项（PTE）时对可缓存内存的支持问题。

在历史讨论中，参与者们探讨了 KVM 如何处理来自 VMA 的 PTE 复制，特别是在物理地址没有对应的结构页时的处理方式。Jason Gunthorpe 提到，当前的 guest_memfd 不会影响直接映射，KVM 不需要创建新的内核映射。讨论中还提到，是否需要一个 KVM 能力（capability）来表明内核是否支持可缓存的 PFNMAP（页面框架号映射）。

在本周的新讨论中，Ankit Agrawal 提出了是否继续保留“可缓存 PFNMAP” KVM 能力的问题。Oliver Upton 强调，用户空间需要了解内存的可缓存性，以便在进行虚拟机迁移时做出正确的决策。他建议将 KVM 能力与内存槽标志结合使用，以确保用户空间期望的 GFN（来宾物理页号）范围能够保证写回语义。Jason Gunthorpe 和 Sean Christopherson 对于增加内存槽标志表示反对，认为这会增加复杂性。

总体而言，讨论围绕如何在 KVM 中有效管理可缓存内存的映射展开，参与者对补丁的必要性和实现方式存在不同看法，尚未达成一致。

#### 📝 邮件列表

1. **[04-07 08:20]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[04-07 13:15]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
3. **[04-07 09:43]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[04-16 08:51]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
5. **[04-21 16:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
6. **[04-22 00:49]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-22 10:54]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
8. **[04-22 07:53]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[04-22 17:50]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[04-22 14:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
11. **[04-22 14:28]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[04-22 20:35]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
13. **[04-23 11:45]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
14. **[04-23 09:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
15. **[04-23 13:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[04-23 10:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 5: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 14:41:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列（PATCH v8 00/43）。该补丁旨在实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 版本中合并。

在历史讨论中，补丁的主要内容包括增加了新的 ioctls 和能力的文档，添加了 "only_private"/"only_shared" 到 kvm 结构中，以及为 RMM（Realm Management Monitor）定义了 SMC 调用的相关内容。补丁还包括对 RMI 调用的包装，以简化错误处理，并在 KVM 初始化时检查 RME（Realm Management Extensions）支持。

在本周的新讨论中，参与者 Suzuki K Poulose 对补丁进行了审查，并提出了一些小的修改建议。他强调了在 RMI 调用中应明确使用 HIPAS 而不是 RMI_ASSIGNED，并确认了相关注释的准确性。此外，他还质疑了在 KVM 初始化时检查 RME 支持的必要性，指出如果主机在虚拟化环境下运行，可能会将调用转发给 RMM。

总体来看，本周讨论主要集中在补丁的审查和一些细节上的澄清，未提出重大变更。

#### 📝 邮件列表

1. **[04-16 14:41]** [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[04-16 14:41]** [PATCH v8 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
3. **[04-16 14:41]** [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
4. **[04-16 14:41]** [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
5. **[04-25 11:30]** Re: [PATCH v8 03/43] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[04-25 11:48]** Re: [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[04-25 11:53]** Re: [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[04-25 12:08]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 6: [PATCH 0/3] KVM: arm64: Address Translation fixes

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 22 Apr 2025 13:26:09 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的地址翻译修复的三个补丁（patch）。这些补丁旨在解决 KVM 地址翻译实现中的多个问题，具体包括错误报告 PAR_EL1.PTW、未处理访问故障以及在特定条件下导致主机崩溃的问题。

在历史讨论中，未提供具体的背景信息，但可以推测这些问题的存在影响了 KVM 的稳定性和功能。

本周的新讨论中，Marc Zyngier 提出了三个补丁：
1. **补丁 1**：修复 PAR_EL1.PTW 和 PAR_EL1.S 的报告逻辑，确保在地址翻译失败时正确反映状态。
2. **补丁 2**：增强地址翻译功能，使其能够处理访问故障，确保在地址翻译过程中能够正确响应权限和访问错误。
3. **补丁 3**：避免在处理 AT S1E{0,1} 时将未初始化的数据传递给 HCR_EL2，从而提高代码的健壮性。

此外，Joey Gouly 对补丁 2 表示支持，并进行了审核，而 D Scott Phillips 提出了关于 TCR_ELx.HA 的依赖性问题，Marc Zyngier 也对此进行了回应，指出当前的配置是支持的。整体来看，本周的讨论集中在补丁的具体实现和潜在的配置依赖性上，推动了 KVM 地址翻译功能的改进。

#### 📝 邮件列表

1. **[04-22 13:26]** [PATCH 0/3] KVM: arm64: Address Translation fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-22 13:26]** [PATCH 1/3] KVM: arm64: Fix PAR_EL1.{PTW,S} reporting on AT S1E*
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-22 13:26]** [PATCH 2/3] KVM: arm64: Teach address translation about access faults
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-22 13:26]** [PATCH 3/3] KVM: arm64: Don't feed uninitialised data to HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-22 14:50]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access
 faults
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[04-22 13:54]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access
 faults
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
7. **[04-22 22:19]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 15 Apr 2025 08:47:10 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对AmpereOne处理器的错误AC03_CPU_36的补丁（PATCH 1/2），该错误可能导致异步异常在特定情况下被错误地路由到错误的异常级别。补丁的核心内容是确保在更新HCR_EL2的控制位时，始终屏蔽异步异常，以避免错误的异常行为。

在历史讨论中，D Scott Phillips提出了补丁，并引用了错误文档，详细描述了在EL2软件更改控制位时可能发生的异常路由问题。Marc Zyngier对此进行了回应，确认了补丁的必要性，并讨论了相关的技术细节。

在本周的新讨论中，D Scott Phillips提出了一个新观点，认为在nvhe模式下，由于异步异常始终被屏蔽，因此该模式下不会遇到此错误。他询问Marc Zyngier对此的看法。Marc Zyngier对此表示认同，并指出在nVHE/hVHE超管代码中，确实通过禁用中断来避免该问题。同时，他提到在处理SError时的特定代码路径也不会引发此错误。最终，Marc表示只需始终设置xMO位，相关的补丁（v2）正在审查中。

总结来看，讨论围绕着补丁的有效性及其在不同模式下的适用性展开，双方达成了一致，认为补丁的实施是合理的。

#### 📝 邮件列表

1. **[04-15 08:47]** [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[04-16 08:19]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-24 19:02]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum
 AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
4. **[04-27 13:21]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH 0/4] KVM: arm64: UBSAN at EL2

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 18:04:30 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中引入 UBSAN（Undefined Behavior Sanitizer）支持的补丁集。补丁的主要目标是使 UBSAN 能够在 EL2 模式下运行，以增强虚拟化环境中的错误检测能力。

在历史讨论中，Mostafa Saleh 提出了补丁集的背景，指出在 EL2 模式下，许多内核支持的 sanitizers 被禁用，而 UBSAN 的引入可以提供更好的错误检测。补丁集包括了 CONFIG_UBSAN_KVM_EL2 的新 Kconfig 选项，允许在受保护的 nvhe/hvhe 模式下启用 UBSAN。Kees Cook 对补丁提出了一些小的格式和命名建议，认为整体上补丁是可行的。

在本周的新讨论中，Mostafa Saleh 回复了 Kees Cook 的反馈，表示将会在补丁的第二版中修正这些小问题。整体来看，讨论进展顺利，补丁集正在朝着完善的方向推进。

#### 📝 邮件列表

1. **[04-16 18:04]** [PATCH 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[04-16 18:04]** [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[04-16 12:54]** Re: [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Kees Cook <kees@kernel.org>
4. **[04-25 17:30]** Re: [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 9: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Apr 2025 13:39:01 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在 VHE 模式下始终将 HCR_EL2.xMO 强制设为 1”。该补丁的目的是解决在 VHE 模式下，物理中断无法正常传递到主机内核的问题，特别是在 HCR_EL2.{TGE,xMO}=={0,0} 的情况下，这会导致中断无法被处理。此外，该补丁还解决了在 AmpereOne 硬件上清除这些位时引发的严重错误（AC03_CPU_36）。

在本周的讨论中，Marc Zyngier 提出了补丁的具体内容，指出了当前设置和清除这些位的做法是多余的，并且可能导致中断处理的问题。D Scott Phillips 在后续邮件中询问是否应当同时删除 `__vgic_v3_get_gic_config()` 中的 xMO 操作。Marc Zyngier 对此表示赞同，并计划对该部分进行修改，准备发布补丁的第二版。

总结而言，本周的讨论集中在补丁的必要性及其潜在影响上，参与者之间的互动显示出对代码质量和系统稳定性的关注。

#### 📝 邮件列表

1. **[04-22 13:39]** [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-24 15:24]** Re: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE
 mode
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
3. **[04-26 19:13]** Re: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 24 Apr 2025 19:47:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 AmpereOne 处理器的 erratum AC04_CPU_23 的补丁（PATCH v2），旨在解决在更新 HCR_EL2 时可能导致的数据地址翻译损坏问题。该补丁通过在写入 HCR_EL2 之前插入 DSB 指令，并在之后插入 ISB 指令，确保旧指令和新指令不会同时处于易损状态，从而避免数据损坏。

在历史讨论中，虽然没有具体的邮件记录，但补丁的背景是针对 AmpereOne 处理器的已知缺陷，补丁的实现细节和必要性得到了参与者的认可。

在本周的新讨论中，D Scott Phillips 提出了补丁的更新版本，主要包括增加了一个 `write_sysreg_hcr()` 辅助函数，并对 erratum 描述进行了更具体的措辞。这些改动旨在提高代码的可读性和可维护性，同时确保补丁的有效性。补丁涉及到多个文件的修改，共计新增 54 行代码，删除 12 行代码，显示出对该问题的重视和解决的积极进展。

#### 📝 邮件列表

1. **[04-24 19:47]** [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

### Thread 11: [PATCH 6.14 227/241] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:44:51 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中启用 EL2 对 FEAT_PMUv3p9 的要求。该补丁（patch）旨在通过添加一个新的初始化助手函数 `__init_el2_fgt2()`，配置与 FEAT_FGT2 相关的细粒度陷阱控制寄存器 HDFGRTR2_EL2 和 HDFGWTR2_EL2，以允许从 EL1 访问 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 寄存器。

在之前的讨论中，补丁的背景是解决在访问这些寄存器时可能导致的陷阱问题，确保在 EL2 环境下能够正确配置相关寄存器以支持性能监控功能。

本周的新讨论中，Greg Kroah-Hartman 提出该补丁为 6.14-stable 版本的审查补丁，并询问是否有任何异议。邮件中没有其他参与者的回复，表明目前没有反对意见，补丁可能会继续推进。

总结而言，此补丁通过增强 EL2 的配置，确保了对新性能监控特性的支持，且目前在邮件列表中未见异议，预计将顺利合并。

#### 📝 邮件列表

1. **[04-23 16:44]** [PATCH 6.14 227/241] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

### Thread 12: [PATCH 6.12 192/223] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:44:24 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁，标题为「[PATCH 6.12 192/223] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9」。该补丁的主要目的是为支持 FEAT_PMUv3p9 的 ARM64 处理器启用 EL2 的相关要求，以确保在 EL1 中访问特定性能监控寄存器（如 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1）时，能够正确配置 EL2 的细粒度陷阱控制寄存器。

在历史讨论中，补丁的背景主要涉及到如何在 EL2 中初始化细粒度陷阱控制寄存器，以便允许对这些寄存器的访问。补丁中新增了一个初始化函数 `__init_el2_fgt2()`，并更新了相关文档以反映这些寄存器的访问要求。

本周的新讨论中，Greg Kroah-Hartman 提出了该补丁的审查请求，询问是否有任何反对意见。补丁已获得 Rob Herring 的测试和审核，表明其在实际应用中的有效性。整体来看，本周的讨论没有新的异议或问题，补丁的推进顺利。

#### 📝 邮件列表

1. **[04-23 16:44]** [PATCH 6.12 192/223] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1

**📧 邮件数**: 39 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 24 Apr 2025 15:13:07 +0100

#### 🤖 AI 总结

本邮件线程讨论了在 KVM 中运行 Qualcomm 的 Gunyah 虚拟机的相关补丁和实现，主要内容如下：

1. **原始补丁/问题内容**：
   该系列补丁（RFC PATCH 00/34）旨在将 Gunyah 虚拟机支持从独立驱动程序接口移植到 KVM，以利用现有的 KVM 基础设施，减少内存管理、IRQ 处理等核心组件的重复工作。

2. **之前讨论要点**：
   之前的讨论集中在 Gunyah 的实现细节上，包括如何处理虚拟机生命周期管理、内存分配和 IRQ 注入等。参与者提到，KVM 的架构接口是内部使用的，不应被用于支持非 KVM 的虚拟化解决方案。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，参与者对补丁的实现进行了深入分析，提出了对 Gunyah 和 KVM 之间关系的看法。Oliver Upton 强调，KVM 不应作为其他虚拟化平台的通用接口，建议 Qualcomm 采用自己的驱动程序。Karim Manaouil 也表示理解这一观点，并认为 Gunyah 的实现仍然对希望在 EL1 中使用 KVM 的用户有价值。最终，Marc Zyngier 进一步支持了这一观点，认为混合这两者是不现实的。

整体来看，尽管补丁展示了将 Gunyah 集成到 KVM 的潜力，但社区对这种集成的可行性和合理性持谨慎态度。

#### 📝 邮件列表

1. **[04-24 15:13]** [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
2. **[04-24 15:13]** [RFC PATCH 01/34] KVM: Allow arch-specific vCPU allocation and freeing
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
3. **[04-24 15:13]** [RFC PATCH 02/34] KVM: irqfd: Add architecture hooks for irqfd allocation and initialization
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
4. **[04-24 15:13]** [RFC PATCH 03/34] KVM: irqfd: Allow KVM backends to override IRQ injection via set_irq callback
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
5. **[04-24 15:13]** [RFC PATCH 04/34] KVM: Add weak stubs for irqchip-related functions for Gunyah builds
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
6. **[04-24 15:13]** [RFC PATCH 05/34] KVM: Add KVM_SET_DTB_ADDRESS ioctl to pass guest DTB address from userspace
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
7. **[04-24 15:13]** [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend support
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
8. **[04-24 15:13]** [RFC PATCH 07/34] KVM: gunyah: Pin guest memory
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
9. **[04-24 15:13]** [RFC PATCH 08/34] docs: gunyah: Introduce Gunyah Hypervisor
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
10. **[04-24 15:13]** [RFC PATCH 09/34] dt-bindings: Add binding for gunyah hypervisor
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
11. **[04-24 15:13]** [RFC PATCH 10/34] gunyah: Common types and error codes for Gunyah hypercalls
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
12. **[04-24 15:13]** [RFC PATCH 11/34] gunyah: Add hypercalls to identify Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
13. **[04-24 15:13]** [RFC PATCH 12/34] gunyah: Add hypervisor driver
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
14. **[04-24 15:13]** [RFC PATCH 13/34] gunyah: Add hypercalls to send and receive messages
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
15. **[04-24 15:13]** [RFC PATCH 14/34] gunyah: Add resource manager RPC core
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
16. **[04-24 15:13]** [RFC PATCH 15/34] gunyah: Add VM lifecycle RPC
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
17. **[04-24 15:13]** [RFC PATCH 16/34] gunyah: Add basic VM lifecycle management
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
18. **[04-24 15:13]** [RFC PATCH 17/34] gunyah: Translate gh_rm_hyp_resource into gunyah_resource
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
19. **[04-24 15:13]** [RFC PATCH 18/34] gunyah: Add resource tickets
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
20. **[04-24 15:13]** [RFC PATCH 19/34] gunyah: Add hypercalls for running a vCPU
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
21. **[04-24 15:13]** [RFC PATCH 20/34] gunyah: add proxy-scheduled vCPUs
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
22. **[04-24 15:13]** [RFC PATCH 21/34] gunyah: Add hypercalls for demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
23. **[04-24 15:13]** [RFC PATCH 22/34] gunyah: Add memory parcel RPC
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
24. **[04-24 15:13]** [RFC PATCH 23/34] gunyah: Add interfaces to map memory into guest address space
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
25. **[04-24 15:13]** [RFC PATCH 24/34] gunyah: Add platform ops on mem_lend/mem_reclaim
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
26. **[04-24 15:13]** [RFC PATCH 25/34] gunyah: Add Qualcomm Gunyah platform ops
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
27. **[04-24 15:13]** [RFC PATCH 26/34] gunyah: Share memory parcels
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
28. **[04-24 15:13]** [RFC PATCH 27/34] gunyah: Share guest VM dtb configuration to Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
29. **[04-24 15:13]** [RFC PATCH 28/34] gunyah: Add RPC to enable demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
30. **[04-24 15:13]** [RFC PATCH 29/34] gunyah: Enable demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
31. **[04-24 15:13]** [RFC PATCH 30/34] gunyah: Add RPC to set VM boot context
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
32. **[04-24 15:13]** [RFC PATCH 31/34] gunyah: allow userspace to set boot cpu context
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
33. **[04-24 15:13]** [RFC PATCH 32/34] gunyah: Add hypercalls for sending doorbell
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
34. **[04-24 15:13]** [RFC PATCH 33/34] KVM: gunyah: Implement irqfd interface
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
35. **[04-24 15:13]** [RFC PATCH 34/34] KVM: gunyah: enable KVM for Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
36. **[04-24 08:34]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
37. **[04-24 09:12]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Trilok Soni <quic_tsoni@quicinc.com>
38. **[04-24 17:43]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
39. **[04-24 17:57]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC] ARM vGIC-ITS tables serialization when running protected VMs

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 14 Apr 2025 12:12:43 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在保护虚拟机（如 pKVM）上运行时，ARM vGIC-ITS 表的序列化问题。最初的补丁（patch）提出了在 KVM 的 ARM 虚拟中断转换服务（ITS）接口中，如何处理设备表、中断转换表和集合表的保存与恢复操作。由于保护虚拟机的主机内核无法访问来宾内存，这引发了对如何安全地处理这些表的讨论。

在历史讨论中，参与者对补丁提出了不同的看法。Marc Zyngier 认为，来宾应确保其内存页对齐，以便超管能够使用，并对补丁表示反对（NAK）。David Woodhouse 则指出，GIC 规范不应隐含地与超管共享整个页面，并认为这种做法存在潜在的安全隐患。

在本周的新讨论中，David Woodhouse 再次强调了对 GIC 规范的担忧，认为低级监视器在 ITS 命令队列上进行监控的实现方式不妥。他建议 KVM 应该将状态传递给用户空间以便迁移，而不是尝试修改 GIC 规范。Marc Zyngier 也表达了对补丁的质疑，认为当前的架构已经足够完善，并质疑补丁所解决的问题的必要性。

总体来看，讨论围绕如何在保护虚拟机环境中安全有效地处理中断表的序列化展开，参与者对补丁的可行性和安全性持有不同意见。

#### 📝 邮件列表

1. **[04-14 12:12]** [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Ilias Stamatis <ilstam@amazon.com>
2. **[04-15 09:35]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-15 10:44]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
4. **[04-22 11:47]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
5. **[04-27 17:37]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-27 17:43]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 13:40:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM 在 arm64 架构下对 MTE（Memory Tagging Extension）功能的支持问题，特别是 MTE_ASYNC 的声明。

**原始 patch/问题的内容**：
Ben Horgan 提出了一个补丁系列，目的是修复当前 KVM 隐藏 ID_AA64PFR1_EL1.MTE_frac 字段的问题。该字段在 ID_AA64PFR1_EL1.MTE==2 的情况下，如果 MTE_frac==0，表示支持 MTE_ASYNC。然而，在没有 MTE_ASYNC 支持的主机上，启用 MTE 功能的来宾会错误地看到 MTE_ASYNC 被声明为支持。

**之前讨论要点**：
在之前的讨论中，Ben Horgan 进一步阐述了补丁的必要性，指出如果 MTE_frac 被无条件屏蔽，来宾将始终看到该值为 0，这可能导致错误的支持声明。因此，他建议将 MTE_frac 的屏蔽条件与 MTE 能力关联，以正确反映主机的支持情况。

**本周的新讨论、进展或结论**：
本周，Marc Zyngier 对补丁提出了质疑，认为不应无条件传播硬件支持的信息，尤其是在 MTE_frac 未来可能演变的情况下。他建议应将修复限制在特定的情况，而不是盲目覆盖来宾对硬件能力的视图。这一讨论表明，尽管补丁的初衷是修复潜在问题，但在实现时需要更加谨慎，以避免未来的不确定性。

#### 📝 邮件列表

1. **[04-14 13:40]** [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[04-14 13:40]** [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[04-27 18:24]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.15, round #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Apr 2025 14:01:58 -0700

#### 🤖 AI 总结

在本次邮件讨论中，主题为 KVM/arm64 的修复补丁，旨在解决 6.15 版本中的启动失败问题，特别是与 PV MIDR 基础设施相关的故障。历史讨论中，Oliver Upton 提出了一个紧急修复补丁，并表示该补丁已获得 Catalin 的审查，建议尽快合并。

在之前的讨论中，Oliver 强调了该补丁的重要性，并请求 Paolo 进行合并，以便在工作周结束前完成处理。

在本周的新讨论中，Paolo Bonzini 回复确认已完成相关工作，并感谢 Oliver 的耐心。这表明补丁的合并工作已经顺利完成，相关问题得到了及时解决。整体来看，此次讨论有效推动了 KVM/arm64 的修复进程，确保了 6.15 版本的稳定性。

#### 📝 邮件列表

1. **[04-18 14:01]** [GIT PULL] KVM/arm64 fixes for 6.15, round #2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[04-24 19:36]** Re: [GIT PULL] KVM/arm64 fixes for 6.15, round #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 14 个 thread

---

### Thread 1: Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.14-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 09:18:09 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”的更新，该补丁已被添加到6.14-stable树中。补丁的主要内容是为FEAT_PMUv3p9特性配置EL2的要求，具体包括初始化细粒度陷阱控制寄存器，以便在EL1中访问PMICNTR_EL0、PMICFILTR_EL0和PMUACR_EL1寄存器。

在历史讨论中，补丁的提交者Anshuman Khandual详细描述了补丁的功能，并指出了相关寄存器的配置需求，确保在EL1访问这些寄存器时不会触发EL2的陷阱。此外，补丁还更新了文档，明确了SCR_EL3.FGTEn2的要求。

在本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到稳定树中，并提供了补丁的链接和文件名。没有其他参与者对此补丁提出异议或进一步讨论，表明该补丁的添加得到了认可。

总的来说，此次补丁的添加旨在增强ARM64架构在处理性能监控方面的能力，确保系统在不同执行级别之间的寄存器访问能够顺利进行。

#### 📝 邮件列表

1. **[04-22 09:18]** Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.14-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 2: Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.12-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 09:16:59 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”的更新，该补丁已被添加到6.12-stable树中。补丁的主要内容是为FEAT_PMUv3p9特性配置EL2的要求，涉及到PMICNTR_EL0、PMICFILTR_EL0和PMUACR_EL1等寄存器的访问控制。补丁中引入了一个新的初始化助手函数`__init_el2_fgt2()`，用于设置EL2的细粒度陷阱控制寄存器，以确保在EL1中访问这些寄存器时不会产生异常。

在历史讨论中，补丁的背景主要集中在FEAT_FGT2的细粒度陷阱控制需求上，讨论了如何正确配置相关寄存器以支持性能监控功能。

本周的新讨论主要是补丁的正式添加通知，参与者Greg Kroah-Hartman确认该补丁已成功加入6.12-stable树，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。整体来看，本周的进展是补丁的顺利合并，未见其他新的讨论或异议。

#### 📝 邮件列表

1. **[04-22 09:16]** Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.12-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 3: Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:55 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁的更新，该补丁标题为“KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN”，已被添加到6.1稳定版本树中。

该补丁的主要内容是移除在VHE模式下，KVM主机内核对CPACR_EL1.ZEN的冗余保存和恢复逻辑。具体来说，当KVM处于VHE模式时，主机内核尝试在vCPU加载和卸载时保存和恢复CPACR_EL1.ZEN的配置，但由于VHE hyp代码在返回主机时会无条件配置CPTR_EL2.ZEN，因此这一逻辑变得多余。补丁的实施使得主机内核可以安全地保存和恢复状态，而无需通过陷阱机制。

在历史讨论中，补丁的背景信息和必要性已被阐明，强调了当前逻辑的冗余性以及主机内核如何处理SVE状态的变化。

本周的新进展是补丁已被正式添加到6.1稳定树中，邮件中还提到，如果有人认为该补丁不应被添加，可以联系稳定邮件列表。整体来看，该补丁的实施旨在简化代码并提高KVM在ARM64架构下的性能和稳定性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 4: Patch "KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:55 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state”添加到6.1稳定版本树中。该补丁旨在解决当前KVM虚拟化环境中，主机的FPSIMD/SVE状态在进入虚拟机时被延迟保存的问题，避免了因状态不一致导致的崩溃和不必要的数据丢失。

在历史讨论中，补丁的背景主要涉及到多个问题，包括主机SVE状态在ptrace修改后被意外丢弃，以及在非保护虚拟机中未能正确保存主机的FPMR值。这些问题自v5.17版本以来就存在，导致了对TIF_SVE标志的错误假设，影响了系统的稳定性。

在本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到6.1稳定树中，并提供了补丁的具体路径和文件名。如果有人认为该补丁不应被添加到稳定树，可以向指定的邮箱反馈。此次补丁的添加标志着对KVM在ARM架构上虚拟化支持的进一步完善，预示着未来可能会有更多相关的修复和优化。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 5: Patch "KVM: arm64: Calculate cptr_el2 traps on activating traps" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁 "KVM: arm64: Calculate cptr_el2 traps on activating traps" 添加到 6.1-stable 树的通知。该补丁的主要内容是，在激活陷阱时从头计算 cptr_el2 的值，避免在每个虚拟 CPU 结构中存储 cptr_el2。这一改动旨在简化代码，并确保某些陷阱（如来宾是否拥有浮点寄存器）在每次虚拟 CPU 运行时都能正确设置。

在历史讨论中，补丁由 Fuad Tabba 提交，并得到了多位开发者的签名支持。补丁的背景是为了修复之前的一个问题，即在 KVM 的 arm64 架构中，cptr_el2 的处理不够灵活，导致了不必要的复杂性。

本周的讨论中，Greg Kroah-Hartman 通知大家该补丁已成功添加到 6.1-stable 树，并提供了补丁文件的链接。邮件中没有其他参与者的回复或异议，表明该补丁的添加得到了认可。

总的来说，本周的进展是补丁的成功合并，标志着对 KVM arm64 的进一步优化。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Calculate cptr_el2 traps on activating traps" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 6: Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN”的更新，该补丁已被添加到6.1-stable树中。

补丁的主要内容是移除在VHE模式下，KVM主机对CPACR_EL1.SMEN的保存和恢复逻辑。历史上，这一逻辑是为了防止在运行vCPU时，主机的SME状态被破坏。然而，随着内核对FPSIMD/SVE/SME状态的处理方式改进，这一逻辑已变得多余且冗长。

在之前的讨论中，补丁的背景信息提到，最初的逻辑是为了处理在VHE模式下主机对SME状态的访问问题，但由于后续的修复，当前的内核已能够安全地处理状态保存和恢复，因此不再需要保存和恢复EL0的SME陷阱状态。

本周的新进展是，补丁已成功添加到6.1-stable树中，参与者Greg Kroah-Hartman通知了这一更新，并邀请其他人如有异议可联系稳定邮件列表。此次更新标志着对KVM在arm64架构下的进一步优化，简化了代码逻辑并提高了系统的稳定性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 7: Patch "KVM: arm64: Remove host FPSIMD saving for non-protected KVM" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁的更新，标题为“**KVM: arm64: 移除非保护模式 KVM 的主机 FPSIMD 保存**”。该补丁已被添加到 6.1-stable 树中。

### 补丁内容
该补丁的主要目的是移除在非保护模式下，KVM 不再需要保存主机的 FPSIMD/SVE/SME 状态，因为主机会主动保存自己的状态。对于保护模式 KVM，仍需保存主机的 FPSIMD/SVE 状态，以防止泄露来宾状态。补丁中删除了未使用的代码和数据结构，并将相关的功能调整到共享的切换头文件中。

### 之前讨论要点
在历史讨论中，补丁的背景信息提到，随着主机对其 FPSIMD/SVE/SME 状态的主动保存，非保护模式下的 KVM 不再需要进行此操作，因此相关代码变得冗余。

### 本周新讨论
本周的讨论主要是通知补丁已成功添加到 6.1-stable 树中，并提供了补丁文件的链接。邮件中没有其他参与者的回复或异议，表明该补丁的添加得到了认可。

总体来看，该补丁的实施旨在简化代码，提升 KVM 的效率，同时确保保护模式下的安全性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove host FPSIMD saving for non-protected KVM" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 8: Patch "KVM: arm64: Refactor exit handlers" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本周的邮件讨论主要围绕一个新的补丁——“KVM: arm64: Refactor exit handlers”，该补丁已被添加到6.1-stable树中。补丁的主要目的是重构ARM64架构下的KVM退出处理程序，以消除头文件对特定C文件的依赖，从而避免编译时的警告。补丁的实现没有功能上的变化，主要是为了提高代码的可维护性和可读性。

在历史讨论中，补丁的作者Mark Rutland详细说明了当前代码的结构问题，指出了由于头文件依赖于C文件中的函数定义，导致在其他文件中使用该头文件时会出现编译警告。补丁经过多位开发者的审查和测试，确保了其质量。

本周的进展是补丁正式被加入到6.1-stable树中，邮件中提到如果有人认为该补丁不应被加入，可以联系稳定性维护团队。整体来看，此次补丁的加入标志着对KVM ARM64代码的进一步优化，提升了代码的整洁性和可用性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Refactor exit handlers" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 9: Patch "KVM: arm64: Mark some header functions as inline" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Mark some header functions as inline”添加到 Linux 6.1 稳定树的通知。

补丁的主要内容是将一些在共享的 hypervisor 切换头文件中的静态函数标记为内联，以避免在未使用这些函数时产生编译器警告。具体来说，这些函数在某些文件中可能未被调用，导致编译器发出未使用函数的警告。通过将这些函数标记为内联，可以消除这些警告，同时不影响功能。

在历史讨论中，补丁的作者 Mark Rutland 提出了这一修改，并得到了多位开发者的审核和认可，包括 Mark Brown 和 Will Deacon。补丁的实现细节包括避免使用 `__alias()`，并使用预处理器宏将某些函数与其他函数关联，以保持代码的一致性。

在本周的新讨论中，Greg Kroah-Hartman 通知大家该补丁已成功添加到 6.1 稳定树。如果任何人认为该补丁不应被添加，可以通过邮件反馈给稳定维护团队。没有其他新的讨论或异议被提出。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Mark some header functions as inline" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 10: Patch "KVM: arm64: Eagerly switch ZCR_EL{1,2}" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“KVM: arm64: Eagerly switch ZCR_EL{1,2}”的更新，该补丁已被添加到6.1-stable树中。补丁的主要目的是在KVM的非保护模式下，确保在虚拟机与主机之间切换时，能够及时切换ZCR_EL{1,2}寄存器的值，以避免在处理软中断时出现状态保存失败的问题。

在历史讨论中，补丁的背景涉及到KVM在处理虚拟机状态时，主机的SVE向量长度（VL）可能与虚拟机的最大VL不一致，导致在某些情况下无法正确保存虚拟机的FPSIMD/SVE状态。补丁通过在虚拟机与主机切换时，主动切换ZCR_EL{1,2}的值，简化了状态管理，避免了对主机SVE使用的陷阱。

本周的新进展是补丁已被正式添加到稳定树中，参与者Greg KH发布了通知，提醒大家如果对此补丁有异议，可以联系稳定邮件列表。此次更新标志着该补丁的正式实施，预示着KVM在ARM64架构下的性能和稳定性将得到提升。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Eagerly switch ZCR_EL{1,2}" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 11: Patch "KVM: arm64: Discard any SVE state when entering KVM guests" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是补丁“KVM: arm64: Discard any SVE state when entering KVM guests”，该补丁已被添加到6.1-stable树中。补丁的主要内容是，在进入KVM虚拟机时，清除任何SVE（Scalable Vector Extension）状态，以确保虚拟机的运行不会受到主机SVE状态的影响。

在历史讨论中，补丁的背景是由于之前的更改（提交8383741ab2e773a99）中，KVM不再跟踪主机的SVE状态，而是依赖于在执行系统调用时禁用SVE。此补丁通过在准备运行虚拟机时清除TIF_SVE标志，并将存储的任务状态转换为FPSIMD格式，以处理未来可能的性能优化问题。

本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到稳定树中，并提供了补丁文件的链接。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。此次讨论没有其他参与者的回复或异议，表明补丁的添加过程顺利。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Discard any SVE state when entering KVM guests" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 12: Patch "arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁的更新，该补丁标题为“arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE”，已被添加到6.1-stable树中。该补丁的主要目的是在保存浮点寄存器状态时，单独跟踪当前使用的FPSIMD状态类型，以便优化系统调用的性能。

在历史讨论中，补丁的背景是现有的状态跟踪依赖于TIF_SVE标志，这限制了在SVE情况下的优化选项。补丁通过引入一个新的枚举类型来明确当前使用的寄存器格式，并在相关的线程结构和KVM客体状态中进行更新。

本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到6.1-stable树，并提供了补丁的文件名和存放位置。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。至此，该补丁的集成标志着对ARM64架构中浮点状态管理的进一步完善，未来可能会有更多功能性改进。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 13: Patch "arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch）“arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM”，该补丁已被添加到 6.1-stable 树中。补丁的主要内容是停止在 KVM 中使用 TIF_SVE 来管理寄存器保存，而是通过明确告知主机浮点代码需要保存哪些寄存器状态来简化 KVM 代码。这一更改旨在优化正常任务的处理，并且不会对功能或性能产生影响。

在之前的讨论中，补丁的作者 Mark Brown 提到，通过移除对 TIF_SVE 的操作，KVM 的代码将变得更简洁，同时确保正确保存所需的数据。该补丁得到了多位开发者的审查和认可。

在本周的新讨论中，Greg Kroah-Hartman 通知大家该补丁已成功添加到稳定树中，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。整体来看，本周的进展主要是补丁的合并通知，没有新的争议或问题提出。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 14: Patch "arm64/fpsimd: Have KVM explicitly say which FP registers to save" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“arm64/fpsimd: Have KVM explicitly say which FP registers to save”添加到 Linux 6.1 稳定树的通知。该补丁的主要目的是简化 KVM 在上下文切换时保存和恢复浮点寄存器的过程，避免不必要的寄存器保存和恢复操作。补丁引入了一个新的枚举值 FP_STATE_CURRENT，允许 KVM 在绑定到 CPU 时明确指定需要保存的寄存器状态。

在之前的讨论中，补丁的背景主要集中在当前 KVM 如何依赖主机的 FPSIMD 代码来管理寄存器的保存与恢复，这种方式虽然有效，但复杂且不够直观。因此，补丁旨在通过让 KVM 显式传递所需的寄存器状态来优化这一过程。

本周的进展是，补丁已被正式添加到 6.1 稳定树中，参与者 Greg KH 通知了这一更新，并提供了补丁的链接。如果有任何人认为该补丁不应被添加到稳定树中，可以向相关邮箱反馈。整体来看，此补丁的添加将有助于提升 KVM 对浮点寄存器管理的效率和清晰度。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Have KVM explicitly say which FP registers to save" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

