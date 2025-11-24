# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-11-24 00:24:29

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 302
- **总 Thread 数**: 29
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 25 threads (270 邮件)
- **RFC**: 1 threads (16 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 2 threads (14 邮件)

---

## 📌 PATCH

共 25 个 thread

---

### Thread 1: [PATCH v4 00/49] KVM: arm64: Add LR overflow infrastructure (the final one, I swear!)

**📧 邮件数**: 51 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Nov 2025 17:24:50 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是「KVM: arm64: 添加 LR 溢出基础设施」，Marc Zyngier 提出了一个包含 49 个补丁的系列更新，旨在改进 ARM64 KVM 的中断处理机制，特别是针对 LR（链接寄存器）溢出的问题。

**原始补丁/问题内容**：
补丁系列的目标是解决 KVM 在处理 ARM64 架构中断时的 LR 溢出问题，确保在中断数量超过 LR 容量时，系统能正确处理这些中断。

**之前讨论要点**：
在之前的讨论中，Marc Zyngier 反复提到补丁的复杂性和多次修正的历史，强调了补丁的必要性和重要性。补丁系列经过多次迭代，整合了许多修复和改进，尤其是在处理 GIC（通用中断控制器）和中断状态管理方面。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的最终版本上，Marc Zyngier 表达了对该系列补丁的信心，并感谢了测试人员的支持。补丁中新增了对 GICv2 和 GICv3 的中断去激活处理、维护中断配置的改进，以及对 LR 溢出处理的详细文档。测试人员 Fuad Tabba 和 Mark Brown 也对补丁进行了验证，确认其在 CI 环境中表现良好。整体来看，此次补丁系列的目标是提升 KVM 在 ARM64 上的中断处理能力，确保在高负载情况下的稳定性和性能。

#### 📝 邮件列表

1. **[11-20 17:24]** [PATCH v4 00/49] KVM: arm64: Add LR overflow infrastructure (the final one, I swear!)
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-20 17:24]** [PATCH v4 01/49] irqchip/gic: Add missing GICH_HCR control bits
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-20 17:24]** [PATCH v4 02/49] irqchip/gic: Expose CPU interface VA to KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-20 17:24]** [PATCH v4 03/49] irqchip/apple-aic: Spit out ICH_MISR_EL2 value on spurious vGIC MI
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-20 17:24]** [PATCH v4 04/49] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-20 17:24]** [PATCH v4 05/49] KVM: arm64: vgic-v3: Fix GICv3 trapping in protected mode
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-20 17:24]** [PATCH v4 06/49] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-20 17:24]** [PATCH v4 07/49] KVM: arm64: Repack struct vgic_irq fields
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-20 17:24]** [PATCH v4 08/49] KVM: arm64: Add tracking of vgic_irq being present in a LR
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[11-20 17:24]** [PATCH v4 09/49] KVM: arm64: Add LR overflow handling documentation
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[11-20 17:25]** [PATCH v4 10/49] KVM: arm64: GICv3: Drop LPI active state when folding LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-20 17:25]** [PATCH v4 11/49] KVM: arm64: GICv3: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[11-20 17:25]** [PATCH v4 12/49] KVM: arm64: GICv3: Decouple ICH_HCR_EL2 programming from LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[11-20 17:25]** [PATCH v4 13/49] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[11-20 17:25]** [PATCH v4 14/49] KVM: arm64: GICv3: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[11-20 17:25]** [PATCH v4 15/49] KVM: arm64: GICv2: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-20 17:25]** [PATCH v4 16/49] KVM: arm64: GICv2: Decouple GICH_HCR programming from LRs being loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[11-20 17:25]** [PATCH v4 17/49] KVM: arm64: GICv2: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[11-20 17:25]** [PATCH v4 18/49] KVM: arm64: GICv2: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-20 17:25]** [PATCH v4 19/49] KVM: arm64: Compute vgic state irrespective of the number of interrupts
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[11-20 17:25]** [PATCH v4 20/49] KVM: arm64: Eagerly save VMCR on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[11-20 17:25]** [PATCH v4 21/49] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[11-20 17:25]** [PATCH v4 22/49] KVM: arm64: Turn kvm_vgic_vcpu_enable() into kvm_vgic_vcpu_reset()
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[11-20 17:25]** [PATCH v4 23/49] KVM: arm64: Make vgic_target_oracle() globally available
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[11-20 17:25]** [PATCH v4 24/49] KVM: arm64: Invert ap_list sorting to push active interrupts out
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[11-20 17:25]** [PATCH v4 25/49] KVM: arm64: Move undeliverable interrupts to the end of ap_list
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[11-20 17:25]** [PATCH v4 26/49] KVM: arm64: Use MI to detect groups being enabled/disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[11-20 17:25]** [PATCH v4 27/49] KVM: arm64: GICv3: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[11-20 17:25]** [PATCH v4 28/49] KVM: arm64: GICv3: Handle deactivation via ICV_DIR_EL1 traps
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[11-20 17:25]** [PATCH v4 29/49] KVM: arm64: GICv3: Add GICv2 SGI handling to deactivation primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[11-20 17:25]** [PATCH v4 30/49] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[11-20 17:25]** [PATCH v4 31/49] KVM: arm64: GICv3: Add SPI tracking to handle asymmetric deactivation
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[11-20 17:25]** [PATCH v4 32/49] KVM: arm64: GICv3: Handle in-LR deactivation when possible
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[11-20 17:25]** [PATCH v4 33/49] KVM: arm64: GICv3: Avoid broadcast kick on CPUs lacking TDIR
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[11-20 17:25]** [PATCH v4 34/49] KVM: arm64: GICv3: nv: Resync LRs/VMCR/HCR early for better MI emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[11-20 17:25]** [PATCH v4 35/49] KVM: arm64: GICv3: nv: Plug L1 LR sync into deactivation primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[11-20 17:25]** [PATCH v4 36/49] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[11-20 17:25]** [PATCH v4 37/49] KVM: arm64: GICv2: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[11-20 17:25]** [PATCH v4 38/49] KVM: arm64: GICv2: Handle deactivation via GICV_DIR traps
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[11-20 17:25]** [PATCH v4 39/49] KVM: arm64: GICv2: Always trap GICV_DIR register
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[11-20 17:25]** [PATCH v4 40/49] KVM: arm64: selftests: gic_v3: Add irq group setting helper
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[11-20 17:25]** [PATCH v4 41/49] KVM: arm64: selftests: gic_v3: Disable Group-0 interrupts by default
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[11-20 17:25]** [PATCH v4 42/49] KVM: arm64: selftests: vgic_irq: Fix GUEST_ASSERT_IAR_EMPTY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[11-20 17:25]** [PATCH v4 43/49] KVM: arm64: selftests: vgic_irq: Change configuration before enabling interrupt
   - 发件人: Marc Zyngier <maz@kernel.org>
45. **[11-20 17:25]** [PATCH v4 44/49] KVM: arm64: selftests: vgic_irq: Exclude timer-controlled interrupts
   - 发件人: Marc Zyngier <maz@kernel.org>
46. **[11-20 17:25]** [PATCH v4 45/49] KVM: arm64: selftests: vgic_irq: Remove LR-bound limitation
   - 发件人: Marc Zyngier <maz@kernel.org>
47. **[11-20 17:25]** [PATCH v4 46/49] KVM: arm64: selftests: vgic_irq: Perform EOImode==1 deactivation in ack order
   - 发件人: Marc Zyngier <maz@kernel.org>
48. **[11-20 17:25]** [PATCH v4 47/49] KVM: arm64: selftests: vgic_irq: Add asymmetric SPI deaectivation test
   - 发件人: Marc Zyngier <maz@kernel.org>
49. **[11-20 17:25]** [PATCH v4 48/49] KVM: arm64: selftests: vgic_irq: Add Group-0 enable test
   - 发件人: Marc Zyngier <maz@kernel.org>
50. **[11-20 17:25]** [PATCH v4 49/49] KVM: arm64: selftests: vgic_irq: Add timer deactivation test
   - 发件人: Marc Zyngier <maz@kernel.org>
51. **[11-21 14:15]** Re: [PATCH v4 00/49] KVM: arm64: Add LR overflow infrastructure (the
 final one, I swear!)
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 2: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the dregs, the bad and the ugly)

**📧 邮件数**: 28 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 17 Nov 2025 09:15:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下添加 LR（Link Register）溢出基础设施的补丁系列。Marc Zyngier 提出了一个包含五个补丁的系列，旨在修复现有的 GICv3（通用中断控制器版本3）实现中的多个问题。

在历史讨论中，Marc 提到之前的补丁系列存在一些缺陷，包括对中断状态的处理不当，以及在 QEMU 环境下的特定行为导致的错误。补丁的主要内容包括：修复在没有配置 vgic 的情况下错误地报告 ICH_HCR_EL2.En 的问题；在 vcpu 退出时完全禁用捕获；改进嵌套 GICv3 支持的状态同步；移除多余的处理遗留代码；以及强制在退出时同步 ICH_HCR_EL2.En。

在本周的新讨论中，Marc 继续更新补丁，并与其他参与者（如 Fuad Tabba 和 Oliver Upton）进行交流。Fuad 表示将对补丁进行测试，并确认其在不同环境下的有效性。多个补丁已获得 Fuad 的审核和测试确认，Marc 计划在下周发布更新版本。

总体而言，本周的讨论集中在补丁的细节修正、测试反馈以及未来的发布计划上，显示出社区对改进 KVM 功能的积极参与。

#### 📝 邮件列表

1. **[11-17 09:15]** [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the dregs, the bad and the ugly)
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-17 09:15]** [PATCH v3 1/5] KVM: arm64: GICv3: Don't advertise ICH_HCR_EL2.En==1 when no vgic is configured
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-17 09:15]** [PATCH v3 2/5] KVM: arm64: GICv3: Completely disable trapping on vcpu exit
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-17 09:15]** [PATCH v3 3/5] KVM: arm64: GICv3: nv: Resync LRs/VMCR/HCR early for better MI emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-17 09:15]** [PATCH v3 4/5] KVM: arm64: GICv3: Remove vgic_hcr workaround handling leftovers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-17 09:15]** [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-17 09:40]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-17 09:54]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the dregs, the bad and the ugly)
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-17 10:18]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[11-17 10:34]** Re: [PATCH v3 1/5] KVM: arm64: GICv3: Don't advertise
 ICH_HCR_EL2.En==1 when no vgic is configured
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[11-17 10:36]** Re: [PATCH v3 2/5] KVM: arm64: GICv3: Completely disable trapping on
 vcpu exit
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[11-17 11:24]** Re: [PATCH v3 3/5] KVM: arm64: GICv3: nv: Resync LRs/VMCR/HCR early
 for better MI emulation
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[11-17 11:25]** Re: [PATCH v3 4/5] KVM: arm64: GICv3: Remove vgic_hcr workaround
 handling leftovers
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[11-17 11:28]** Re: [PATCH v3 1/5] KVM: arm64: GICv3: Don't advertise ICH_HCR_EL2.En==1 when no vgic is configured
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[11-17 11:29]** Re: [PATCH v3 1/5] KVM: arm64: GICv3: Don't advertise
 ICH_HCR_EL2.En==1 when no vgic is configured
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[11-17 11:34]** Re: [PATCH v3 3/5] KVM: arm64: GICv3: nv: Resync LRs/VMCR/HCR early for better MI emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-17 11:35]** Re: [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[11-17 11:37]** Re: [PATCH v3 3/5] KVM: arm64: GICv3: nv: Resync LRs/VMCR/HCR early
 for better MI emulation
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[11-17 11:42]** Re: [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-17 11:48]** Re: [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[11-17 12:54]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[11-17 23:16]** Re: [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync
 ICH_HCR_EL2.En
   - 发件人: Oliver Upton <oupton@kernel.org>
23. **[11-17 23:20]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Oliver Upton <oupton@kernel.org>
24. **[11-18 08:54]** Re: [PATCH v3 5/5] KVM: arm64: GICv3: Force exit to sync ICH_HCR_EL2.En
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[11-18 13:59]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Fuad Tabba <tabba@google.com>
26. **[11-18 19:06]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the dregs, the bad and the ugly)
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[11-18 15:34]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the dregs, the bad and the ugly)
   - 发件人: Oliver Upton <oupton@kernel.org>
28. **[11-19 10:37]** Re: [PATCH v3 0/5] KVM: arm64: Add LR overflow infrastructure (the
 dregs, the bad and the ugly)
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 3: [PATCH v5 00/27] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)

**📧 邮件数**: 28 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 17 Nov 2025 18:47:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 ARM SMMUv3 驱动的多个补丁（PATCH v5 00/27），主要集中在虚拟化和内存管理方面的改进。以下是讨论的主要内容：

1. **原始补丁内容**：补丁系列旨在为 KVM 提供 ARM SMMUv3 驱动，支持在受保护的虚拟机环境中进行内存隔离和设备管理。补丁包括命令队列（CMDQ）和流表（STE）的仿真，确保虚拟机能够安全地与硬件交互。

2. **历史讨论要点**：之前的讨论涵盖了 SMMUv3 驱动的设计理念，包括如何在虚拟化环境中处理设备的内存访问、命令队列的管理及其与主机的交互。补丁的设计考虑了性能和安全性，确保主机无法直接访问虚拟机的内存。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现细节上，包括：
   - 增加了对 CMDQ 和 STE 的仿真逻辑，确保主机与虚拟机之间的命令和状态同步。
   - 实现了对流表的影子管理，允许在主机和虚拟机之间安全地共享和更新流表。
   - 讨论了如何在 SMMU 启用和禁用时管理命令队列和流表的共享状态。
   - 引入了对 IOMMU 的支持，确保在虚拟化环境中能够有效地管理内存和设备访问。

总的来说，本线程的讨论展示了如何通过补丁系列增强 KVM 的 ARM SMMUv3 驱动，以支持更复杂的虚拟化需求，确保在保护模式下的安全性和性能。

#### 📝 邮件列表

1. **[11-17 18:47]** [PATCH v5 00/27] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[11-17 18:47]** [PATCH v5 01/27] KVM: arm64: Add a new function to donate memory with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[11-17 18:47]** [PATCH v5 02/27] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[11-17 18:47]** [PATCH v5 03/27] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[11-17 18:47]** [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific code out
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[11-17 18:47]** [PATCH v5 05/27] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[11-17 18:47]** [PATCH v5 06/27] iommu/arm-smmu-v3: Move TLB range invalidation into
 common code
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[11-17 18:47]** [PATCH v5 07/27] iommu/arm-smmu-v3: Move IDR parsing to common functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[11-17 18:47]** [PATCH v5 08/27] KVM: arm64: iommu: Introduce IOMMU driver infrastructure
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[11-17 18:47]** [PATCH v5 09/27] KVM: arm64: iommu: Shadow host stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[11-17 18:47]** [PATCH v5 10/27] KVM: arm64: iommu: Add memory pool
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[11-17 18:47]** [PATCH v5 11/27] KVM: arm64: iommu: Support DABT for IOMMU
   - 发件人: Mostafa Saleh <smostafa@google.com>
13. **[11-17 18:47]** [PATCH v5 12/27] iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
14. **[11-17 18:48]** [PATCH v5 13/27] iommu/arm-smmu-v3-kvm: Add the kernel driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
15. **[11-17 18:48]** [PATCH v5 14/27] iommu/arm-smmu-v3: Support probing KVM emulated devices
   - 发件人: Mostafa Saleh <smostafa@google.com>
16. **[11-17 18:48]** [PATCH v5 15/27] iommu/arm-smmu-v3-kvm: Create array for hyp SMMUv3
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[11-17 18:48]** [PATCH v5 16/27] iommu/arm-smmu-v3-kvm: Take over SMMUs
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[11-17 18:48]** [PATCH v5 17/27] iommu/arm-smmu-v3-kvm: Probe SMMU HW
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[11-17 18:48]** [PATCH v5 18/27] iommu/arm-smmu-v3-kvm: Add MMIO emulation
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[11-17 18:48]** [PATCH v5 19/27] iommu/arm-smmu-v3-kvm: Shadow the command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[11-17 18:48]** [PATCH v5 20/27] iommu/arm-smmu-v3-kvm: Add CMDQ functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[11-17 18:48]** [PATCH v5 21/27] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[11-17 18:48]** [PATCH v5 22/27] iommu/arm-smmu-v3-kvm: Shadow stream table
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[11-17 18:48]** [PATCH v5 23/27] iommu/arm-smmu-v3-kvm: Shadow STEs
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[11-17 18:48]** [PATCH v5 24/27] iommu/arm-smmu-v3-kvm: Emulate GBPA
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[11-17 18:48]** [PATCH v5 25/27] iommu/arm-smmu-v3-kvm: Support io-pgtable
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[11-17 18:48]** [PATCH v5 26/27] iommu/arm-smmu-v3-kvm: Shadow the CPU stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[11-17 18:48]** [PATCH v5 27/27] iommu/arm-smmu-v3-kvm: Enable nesting
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 4: [PATCH v2 00/11] TSM: Implement ->lock()/->accept() callbacks for ARM CCA TDISP setup

**📧 邮件数**: 23 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 17 Nov 2025 19:29:56 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM CCA（Confidential Computing Architecture）设备的补丁系列，主要实现了 TSM（Trust Security Manager）接口的锁定和接受回调功能，以支持 TDISP（Trusted Device Interface）设置。

**原始补丁内容**：
补丁系列（共11个）实现了 TSM 的 `->lock()`、`->unlock()` 和 `->accept()` 回调，符合 RMM ALP17 规范的要求。补丁的目的是增强 ARM CCA 设备的安全性和功能性。

**历史讨论要点**：
在之前的讨论中，补丁的设计和实现细节得到了初步的审查，参与者提出了一些关于代码清晰性和一致性的建议，强调了代码中类型匹配和错误处理的规范性。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现和代码审查上。Aneesh Kumar K.V 提交了多个补丁，涵盖了设备的锁定、解锁、状态转换、接口报告更新、测量获取和设备信息验证等功能。Jonathan Cameron 对补丁提供了反馈，建议在代码中增加注释和清晰的变量作用域，确保代码的可读性和维护性。此外，部分补丁已获得审核通过，标志着该系列补丁的逐步完善。

总体来看，此次讨论推动了 ARM CCA 设备的安全性和功能性提升，同时也加强了代码的规范性和可维护性。

#### 📝 邮件列表

1. **[11-17 19:29]** [PATCH v2 00/11] TSM: Implement ->lock()/->accept() callbacks for ARM CCA TDISP setup
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[11-17 19:29]** [PATCH v2 01/11] coco: guest: arm64: Guest TSM callback and realm device lock support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[11-17 19:29]** [PATCH v2 02/11] coco: guest: arm64: Add Realm Host Interface and guest DA helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[11-17 19:29]** [PATCH v2 03/11] coco: guest: arm64: Add support for guest initiated TDI bind/unbind
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[11-17 19:30]** [PATCH v2 04/11] coco: guest: arm64: Add support for updating interface reports from device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[11-17 19:30]** [PATCH v2 05/11] coco: guest: arm64: Add support for updating measurements from device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[11-17 19:30]** [PATCH v2 06/11] coco: guest: arm64: Add support for reading cached objects from host
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[11-17 19:30]** [PATCH v2 07/11] coco: guest: arm64: Validate Realm MMIO mappings from TDISP report
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[11-17 19:30]** [PATCH v2 08/11] coco: guest: arm64: Add support for fetching and verifying device info
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[11-17 19:30]** [PATCH v2 09/11] coco: guest: arm64: Wire Realm TDISP RUN/STOP transitions into guest driver
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[11-17 19:30]** [PATCH v2 10/11] coco: arm64: dma: Update force_dma_unencrypted for accepted devices
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[11-17 19:30]** [PATCH v2 11/11] coco: guest: arm64: Enable vdev DMA after attestation
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[11-19 15:22]** Re: [PATCH v2 01/11] coco: guest: arm64: Guest TSM callback and
 realm device lock support
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
14. **[11-19 15:32]** Re: [PATCH v2 02/11] coco: guest: arm64: Add Realm Host Interface
 and guest DA helper
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
15. **[11-19 15:50]** Re: [PATCH v2 03/11] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
16. **[11-19 15:54]** Re: [PATCH v2 04/11] coco: guest: arm64: Add support for updating
 interface reports from device
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
17. **[11-20 15:22]** Re: [PATCH v2 05/11] coco: guest: arm64: Add support for updating
 measurements from device
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
18. **[11-20 17:31]** Re: [PATCH v2 06/11] coco: guest: arm64: Add support for reading
 cached objects from host
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
19. **[11-20 17:43]** Re: [PATCH v2 07/11] coco: guest: arm64: Validate Realm MMIO
 mappings from TDISP report
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
20. **[11-20 17:54]** Re: [PATCH v2 08/11] coco: guest: arm64: Add support for fetching
 and verifying device info
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
21. **[11-20 17:55]** Re: [PATCH v2 09/11] coco: guest: arm64: Wire Realm TDISP RUN/STOP
 transitions into guest driver
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
22. **[11-20 17:58]** Re: [PATCH v2 10/11] coco: arm64: dma: Update force_dma_unencrypted
 for accepted devices
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
23. **[11-20 17:59]** Re: [PATCH v2 11/11] coco: guest: arm64: Enable vdev DMA after
 attestation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>

---

### Thread 5: [PATCH v2 00/14] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF

**📧 邮件数**: 21 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 17 Nov 2025 14:43:11 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现 FEAT_XNX 和 FEAT_HAF 的补丁系列（PATCH v2 00/14）。该补丁的主要目标是支持新的硬件特性，以增强虚拟化性能。

**原始补丁/问题内容**：
补丁系列旨在实现 FEAT_XNX 和 FEAT_HAF，这些特性涉及到对虚拟机的权限管理和访问标志的处理。补丁中包括对页表库的修改，以支持新的执行权限编码。

**之前的讨论要点**：
在之前的讨论中，参与者对补丁的实现细节进行了探讨，尤其是对描述符的处理和权限的管理。讨论中提到了一些潜在的错误和改进建议，例如对未初始化变量的处理和对描述符的正确更新。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，Oliver Upton 提供了多个补丁的更新和修复建议，包括对变量初始化、错误处理和代码清理的建议。Marc Zyngier 也提出了一些关于代码逻辑和锁定机制的改进意见。总体来看，尽管存在一些需要解决的错误，但对补丁系列的整体结构表示认可，并希望能尽快重新提交以便在后续版本中进行测试。

#### 📝 邮件列表

1. **[11-17 14:43]** [PATCH v2 00/14] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-17 14:43]** [PATCH v2 01/14] arm64: Detect FEAT_XNX
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-17 14:43]** [PATCH v2 02/14] KVM: arm64: Add support for FEAT_XNX stage-2 permissions
   - 发件人: Oliver Upton <oupton@kernel.org>
4. **[11-17 14:43]** [PATCH v2 03/14] KVM: arm64: nv: Forward FEAT_XNX permissions to the shadow stage-2
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[11-17 14:43]** [PATCH v2 04/14] KVM: arm64: Teach ptdump about FEAT_XNX permissions
   - 发件人: Oliver Upton <oupton@kernel.org>
6. **[11-17 14:43]** [PATCH v2 05/14] KVM: arm64: nv: Advertise support for FEAT_XNX
   - 发件人: Oliver Upton <oupton@kernel.org>
7. **[11-17 14:43]** [PATCH v2 06/14] KVM: arm64: Call helper for reading descriptors directly
   - 发件人: Oliver Upton <oupton@kernel.org>
8. **[11-17 14:43]** [PATCH v2 07/14] KVM: arm64: Handle endianness in read helper for emulated PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
9. **[11-17 14:43]** [PATCH v2 08/14] KVM: arm64: nv: Use pgtable definitions in stage-2 walk
   - 发件人: Oliver Upton <oupton@kernel.org>
10. **[11-17 14:43]** [PATCH v2 09/14] KVM: arm64: Add helper for swapping guest descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>
11. **[11-17 14:43]** [PATCH v2 10/14] KVM: arm64: Propagate PTW errors up to AT emulation
   - 发件人: Oliver Upton <oupton@kernel.org>
12. **[11-17 14:43]** [PATCH v2 11/14] KVM: arm64: Implement HW access flag management in stage-1 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
13. **[11-17 14:43]** [PATCH v2 12/14] KVM: arm64: nv: Implement HW access flag management in stage-2 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
14. **[11-17 14:43]** [PATCH v2 13/14] KVM: arm64: nv: Expose hardware access flag management to NV guests
   - 发件人: Oliver Upton <oupton@kernel.org>
15. **[11-17 14:43]** [PATCH v2 14/14] KVM: arm64: selftests: Add test for AT emulation
   - 发件人: Oliver Upton <oupton@kernel.org>
16. **[11-21 12:24]** Re: [PATCH v2 02/14] KVM: arm64: Add support for FEAT_XNX stage-2 permissions
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-21 17:10]** Re: [PATCH v2 06/14] KVM: arm64: Call helper for reading descriptors directly
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[11-21 17:40]** Re: [PATCH v2 07/14] KVM: arm64: Handle endianness in read helper for emulated PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[11-21 18:25]** Re: [PATCH v2 09/14] KVM: arm64: Add helper for swapping guest descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-21 18:37]** Re: [PATCH v2 12/14] KVM: arm64: nv: Implement HW access flag management in stage-2 SW PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[11-21 18:43]** Re: [PATCH v2 00/14] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 21 Nov 2025 17:23:37 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv9.5 引入的硬件脏状态跟踪结构（HDBSS）特性的支持，包含五个补丁的更新。

1. **原始补丁内容**：补丁系列旨在实现 HDBSS 特性，优化翻译表描述符的脏状态跟踪，降低实时迁移的开销。HDBSS 类似于英特尔的页面修改日志（PML），为 ARM 提供硬件辅助的脏状态跟踪。

2. **之前讨论要点**：历史讨论中提到，HDBSS 的实现需要对系统架构进行相应的支持和注册信息的添加。补丁的初版在三月时提交，随后有多位参与者提出了反馈，但未得到及时回复。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现和改进上。参与者对补丁的变更进行了详细审查，提出了对代码结构、错误处理和功能实现的多项建议。补丁的更新版本（v2）已对之前的反馈进行了部分响应，修正了冗余的宏定义，分离了接口和实现，并整合了系统支持检测。尽管补丁有进展，但仍有参与者对实现的细节表示担忧，认为错误处理和内存管理方面存在问题，呼吁更严格的测试和审查。

#### 📝 邮件列表

1. **[11-21 17:23]** [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
2. **[11-21 17:23]** [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
3. **[11-21 17:23]** [PATCH v2 2/5] KVM: arm64: Support set the DBM attr during memory abort
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
4. **[11-21 17:23]** [PATCH v2 3/5] KVM: arm64: Add support for FEAT_HDBSS
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
5. **[11-21 17:23]** [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
6. **[11-21 17:23]** [PATCH v2 5/5] KVM: arm64: Document HDBSS ioctl
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
7. **[11-21 09:54]** Re: [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-21 18:21]** Re: [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: z00939249 <zhengtian10@huawei.com>
9. **[11-22 12:40]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[11-22 12:54]** Re: [PATCH v2 2/5] KVM: arm64: Support set the DBM attr during memory abort
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[11-22 13:25]** Re: [PATCH v2 3/5] KVM: arm64: Add support for FEAT_HDBSS
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-22 16:17]** Re: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[11-22 16:23]** Re: [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v8 00/28] Tracefs support for pKVM

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Nov 2025 09:38:12 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 pKVM 添加 Tracefs 支持的补丁系列（PATCH v8 00/28）。该补丁旨在为保护模式下的虚拟机监控器（hypervisor）提供调试和分析工具，Tracefs 被认为是一个理想的选择，因为它简单易用，并且支持多种工具。

在历史讨论中，Vincent Donnefort 提出了多个补丁，包括支持未对齐的 fixmap、添加时钟支持、以及为 pKVM 提供跟踪能力等。这些补丁的目标是增强 hypervisor 的可调试性和性能分析能力，尤其是在保护模式下。

在本周的新讨论中，Marc Zyngier 对多个补丁提出了具体的反馈和建议。例如，他对补丁 19 提出了关于返回值的疑问，认为 fixmap_map_slot() 应该返回一个 slot，而不是其中的内容。对于补丁 20，他指出了使用物理计数器的潜在问题，并建议增加文档说明。对于补丁 21，他对数据类型的选择和命名提出了质疑，并建议将其与 NVHE_EL2_DEBUG 相关联。最后，他对补丁 22 的命名和功能提出了改进意见，认为可以使用更准确的术语。

总体来看，本周的讨论集中在对补丁的细节审查和改进建议上，显示出参与者对增强 pKVM 功能的关注和对代码质量的严格要求。

#### 📝 邮件列表

1. **[11-07 09:38]** [PATCH v8 00/28] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[11-07 09:38]** [PATCH v8 19/28] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[11-07 09:38]** [PATCH v8 20/28] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[11-07 09:38]** [PATCH v8 21/28] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[11-07 09:38]** [PATCH v8 22/28] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[11-19 15:38]** Re: [PATCH v8 19/28] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-19 15:44]** Re: [PATCH v8 20/28] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-19 17:06]** Re: [PATCH v8 21/28] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-19 17:31]** Re: [PATCH v8 22/28] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[11-20 09:55]** Re: [PATCH v8 19/28] KVM: arm64: Support unaligned fixmap in the
 pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[11-20 11:36]** Re: [PATCH v8 20/28] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[11-20 12:01]** Re: [PATCH v8 21/28] KVM: arm64: Add tracing capability for the pKVM
 hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[11-20 12:27]** Re: [PATCH v8 22/28] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 8: [PATCH v5 0/9] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Nov 2025 10:37:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁系列，主要集中在来宾 CPU 特性捕获和启用方面。Fuad Tabba 提出了一个包含九个补丁的系列，旨在解决与受保护虚拟机（pKVM）相关的多个问题。

在历史讨论中，补丁系列的背景是为了修复受保护虚拟机中对特定 CPU 特性的捕获和启用逻辑。补丁内容包括修复 Trace Buffer 捕获、MTE（内存标签扩展）标志初始化等问题。

本周的新讨论中，Fuad 提供了补丁的具体实现细节，包括：
1. 修复了受保护虚拟机中 Trace Buffer 捕获的极性问题。
2. 修正了 MTE 标志的初始化逻辑，确保只有在允许的情况下才会设置该标志。
3. 引入了新的辅助函数以提高代码可读性，并跟踪 KVM IOCTL 与其关联的能力。
4. 明确禁止在受保护模式下为任何虚拟机启用 MTE，以减少复杂性。
5. 增强了对 VM 能力检查的逻辑，确保只有在支持的情况下才允许特定的 IOCTL。

此外，补丁系列得到了相关人员的审查和认可，显示出社区对这些修复的积极反馈。整体而言，这些补丁旨在提高 KVM 在 arm64 架构下的稳定性和安全性。

#### 📝 邮件列表

1. **[11-18 10:37]** [PATCH v5 0/9] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[11-18 10:37]** [PATCH v5 1/9] KVM: arm64: Fix Trace Buffer trapping for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[11-18 10:37]** [PATCH v5 2/9] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-18 10:38]** [PATCH v5 3/9] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[11-18 10:38]** [PATCH v5 4/9] KVM: arm64: Introduce helper to calculate fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-18 10:38]** [PATCH v5 5/9] KVM: arm64: Include VM type when checking VM
 capabilities in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[11-18 10:38]** [PATCH v5 6/9] KVM: arm64: Do not allow KVM_CAP_ARM_MTE for any guest
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-18 10:38]** [PATCH v5 7/9] KVM: arm64: Track KVM IOCTLs and their associated KVM caps
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[11-18 10:38]** [PATCH v5 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[11-18 10:38]** [PATCH v5 9/9] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[11-18 10:39]** Re: [PATCH v5 0/9] KVM: arm64: Fixes for guest CPU feature trapping
 and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[11-18 11:11]** Re: [PATCH v5 2/9] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 9: [PATCH v3 0/2]  arm: add kvm-psci-version vcpu property

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 12 Nov 2025 19:13:55 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM 架构的 KVM 中添加 `kvm-psci-version` vcpu 属性的补丁（PATCH v3 0/2）。该补丁旨在允许用户请求特定的 PSCI 版本，以支持在不同默认 PSCI 版本的主机内核之间进行迁移。

在历史讨论中，Sebastian Ott 提出了该补丁的背景，强调了支持 PSCI v0.1 的必要性，并指出在这种情况下需要放弃使用 `KVM_CAP_ARM_PSCI_0_2` 进行 vcpu 初始化。Philippe Mathieu-Daudé 提出了对枚举 PSCI 版本的建议，Sebastian 也回应了关于代码维护的考虑。

在本周的新讨论中，Eric Auger 表达了对补丁的支持，并建议将属性名称加上 `kvm_` 前缀，以便与其他 KVM 元素保持一致。Philippe 和其他参与者也表示同意，认为补丁看起来不错。Sebastian 进一步澄清了补丁中列出的 PSCI 版本是一个不完整的列表，未来新版本的引入不需要更改现有代码。

总体来看，本周的讨论主要集中在补丁的命名和代码维护方面，参与者对补丁的方向表示支持，且没有提出重大的异议。

#### 📝 邮件列表

1. **[11-12 19:13]** [PATCH v3 0/2]  arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[11-12 19:13]** [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[11-12 22:07]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: =?UTF-8?Q?Philippe_Mathieu-Daud=C3=A9?= <philmd@linaro.org>
4. **[11-13 13:05]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>
5. **[11-19 02:07]** [PATCH v3 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[11-19 02:07]** [PATCH v3 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[11-19 02:07]** [PATCH v3 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
8. **[11-20 11:10]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
9. **[11-20 11:11]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
10. **[11-20 11:43]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: =?UTF-8?Q?Philippe_Mathieu-Daud=C3=A9?= <philmd@linaro.org>
11. **[11-20 14:11]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 10: [PATCH 00/12] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 12 Nov 2025 10:33:54 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现 FEAT_XNX 和 FEAT_HAF 特性的补丁系列。历史讨论中，Oliver Upton 提出了多个补丁，主要目标是填补 KVM 的影子二级页表实现与架构之间的差距。FEAT_XNX 主要涉及在伪 TLB 中表达特权和非特权执行权限，而 FEAT_HAF 则需要在用户内存中原子性地更新描述符以设置访问标志。

在之前的讨论中，参与者们关注了补丁的实现细节，包括如何处理描述符的交换和访问标志的管理。Oliver 提到需要在 KVM 的软件页表中实现对访问标志的管理，并对不同的上下文进行相应的处理。

在本周的新讨论中，Marc Zyngier 对几个补丁提出了具体的改进建议，指出了代码中的一些潜在问题，如描述符未初始化的情况和异常处理的缺失。他建议在进行功能性更改之前，先进行代码重构。尽管存在一些问题，Marc 对某些部分表示认可，并希望在修复后尽快将这些补丁纳入 6.19 版本。Oliver 对反馈表示感谢，并承诺会进行相应的修改。整体来看，本周的讨论集中在代码质量和功能实现的细节上。

#### 📝 邮件列表

1. **[11-12 10:33]** [PATCH 00/12] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-12 10:34]** [PATCH 09/12] KVM: arm64: Add helper for swapping guest descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-12 10:34]** [PATCH 10/12] KVM: arm64: Implement HW access flag management in stage-1 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
4. **[11-12 10:34]** [PATCH 11/12] KVM: arm64: nv: Implement HW access flag management in stage-2 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[11-17 14:14]** Re: [PATCH 09/12] KVM: arm64: Add helper for swapping guest descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-17 14:49]** Re: [PATCH 10/12] KVM: arm64: Implement HW access flag management in stage-1 SW PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-17 14:51]** Re: [PATCH 11/12] KVM: arm64: nv: Implement HW access flag management in stage-2 SW PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-17 15:21]** Re: [PATCH 00/12] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-17 09:53]** Re: [PATCH 10/12] KVM: arm64: Implement HW access flag management in
 stage-1 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
10. **[11-17 10:13]** Re: [PATCH 09/12] KVM: arm64: Add helper for swapping guest
 descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 11: [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 7 Nov 2025 15:21:20 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于为 Armv8.7 架构添加对 FEAT_{LS64, LS64_V} 的支持及相关测试的补丁（PATCH v7 0/7）。该补丁旨在实现单拷贝原子 64 字节加载和存储指令的支持，包括在 CPU 功能列表中识别和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露支持情况、添加相关的硬件能力测试，并处理虚拟机中对不支持的内存访问的异常。

在历史讨论中，参与者对补丁的安全性提出了质疑，尤其是用户空间是否应当直接暴露这些特性。Marc Zyngier 指出，用户空间可能会伪造某些数据，导致安全隐患。Zhou Wang 和 Arnd Bergmann 进一步讨论了 ST64BV 和 ST64BV0 指令的实现细节，强调了在特定硬件环境下的安全性和兼容性问题。

在本周的新讨论中，Zhou Wang 确认了其系统不支持 ST64BV0，因此不会出现相关的非法指令异常。Arnd Bergmann 建议在内核启动时根据平台配置选择使用 ST64BV 或 ST64BV0，并提出了对 IOMMU 设备绑定的修改建议，以确保兼容性和安全性。这些讨论为补丁的进一步开发和测试提供了重要的方向和思路。

#### 📝 邮件列表

1. **[11-07 15:21]** [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[11-07 15:21]** [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[11-11 11:15]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-13 22:40]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[11-13 17:26]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
6. **[11-14 17:25]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
7. **[11-14 10:37]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
8. **[11-18 10:31]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
9. **[11-18 08:36]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 12: [PATCH 0/5] KVM: arm64: Add support for FEAT_IDST

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Nov 2025 13:31:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上新增的特性 FEAT_IDST 的支持。该特性出现在 ARMv8.4 中，允许对未实现的 ID 寄存器进行捕获，涉及 GMID_EL1、CCSIDR2_EL1 和 SMIDR_EL1 三个寄存器。

在历史讨论中，参与者 Marc Zyngier 提出了一个补丁系列（共五个补丁），旨在实现对这些寄存器的特定处理，并在 KVM 中添加自测试以确保其功能正常。补丁的主要内容包括：为 GMID_EL1 添加路由和处理、在缺少 MTE（Memory Tagging Extension）的情况下强制捕获 GMID_EL1、引入通用的同步异常注入原语、以及在捕获未实现的系统寄存器时使用特定的异常代码（EC=0x18）。

在本周的新讨论中，Marc Zyngier 继续提交了补丁，并得到了参与者 Joey Gouly 的审阅和确认，确保了对 GMID_EL1 捕获的实现不依赖于 CONFIG_ARM64_MTE 的配置。补丁的测试部分也得到了完善，确保在没有 MTE、SME 和 CCIDX 的虚拟机环境中，能够正确捕获并处理相关寄存器的访问。整体进展顺利，补丁系列正在向合并推进。

#### 📝 邮件列表

1. **[11-20 13:31]** [PATCH 0/5] KVM: arm64: Add support for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-20 13:31]** [PATCH 1/5] KVM: arm64: Add routing/handling for GMID_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-20 13:31]** [PATCH 2/5] KVM: arm64: Force trap of GMID_EL1 when the guest doesn't have MTE
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-20 13:32]** [PATCH 3/5] KVM: arm64: Add a generic synchronous exception injection primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-20 13:32]** [PATCH 4/5] KVM: arm64: Report optional ID register traps with a 0x18 syndrome
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-20 13:32]** [PATCH 5/5] KVM: arm64: selftests: Add a test for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-20 14:34]** Re: [PATCH 2/5] KVM: arm64: Force trap of GMID_EL1 when the guest
 doesn't have MTE
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[11-20 14:51]** Re: [PATCH 2/5] KVM: arm64: Force trap of GMID_EL1 when the guest doesn't have MTE
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation

**📧 邮件数**: 8 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 19 Nov 2025 01:38:20 -0800

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH 0/2] KVM: arm64: 修复 KVM 结构体分配”，主要集中在对 KVM 结构体分配的修复和优化。

1. **原始 patch/问题内容**：本次补丁主要包含两个部分：第一部分是移除 KVM 结构体分配中的 `__GFP_HIGHMEM` 标志，因为这个标志在当前上下文中没有意义，并且会导致 `vmalloc()` 函数发出警告；第二部分是使用 `kvzalloc()` 进行 KVM 结构体的分配，以提高性能。

2. **之前讨论要点**：在历史讨论中，未提及具体的背景信息，但可以推测出该问题是由于最近对 `vmalloc()` 的更改引发的警告，Nathan Chancellor 提出了这一问题。

3. **本周的新讨论、进展或结论**：本周的讨论中，Oliver Upton 提出了两个补丁，得到了参与者的积极反馈，包括 Joey Gouly、Marc Zyngier 和 Vishal Moola 等人均表示支持并进行了审核。最终，Oliver Upton 确认已将补丁应用到下一个版本中，并感谢了测试者 Nathan Chancellor 的反馈。这表明该补丁已获得广泛认可，并将提升 KVM 的内存分配效率。

#### 📝 邮件列表

1. **[11-19 01:38]** [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-19 01:38]** [PATCH 1/2] KVM: arm64: Drop useless __GFP_HIGHMEM from kvm struct allocation
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-19 01:38]** [PATCH 2/2] KVM: arm64: Use kvzalloc() for kvm struct allocation
   - 发件人: Oliver Upton <oupton@kernel.org>
4. **[11-19 10:32]** Re: [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[11-19 13:08]** Re: [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-19 11:12]** Re: [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation
   - 发件人: Vishal Moola (Oracle) <vishal.moola@gmail.com>
7. **[11-19 14:35]** Re: [PATCH 0/2] KVM: arm64: Fixes to KVM struct allocation
   - 发件人: Oliver Upton <oupton@kernel.org>
8. **[11-20 00:08]** Re: [PATCH 1/2] KVM: arm64: Drop useless __GFP_HIGHMEM from kvm
 struct allocation
   - 发件人: Nathan Chancellor <nathan@kernel.org>

---

### Thread 14: [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Sun,  9 Nov 2025 17:15:34 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构中添加 LR（Link Register）溢出基础设施的补丁（PATCH v2 00/45）。该补丁旨在修复一些与 vgic（虚拟通用中断控制器）相关的严重错误，并已在多种硬件上进行了广泛测试。

在历史讨论中，Marc Zyngier 提出了补丁的第二个版本，强调了其在修复 vgic 错误和优化性能方面的重要性。Fuad Tabba 在后续邮件中报告了在测试中遇到的 0x18 陷阱问题，并讨论了可能的原因，认为这可能与 QEMU 的处理方式有关。

在本周的新讨论中，Fuad 和 Marc 继续探讨了陷阱问题的根源。Fuad 表示，问题可能与 gic_eoimode1_eoi_irq() 函数中的处理有关，而 Marc 则确认该问题与特定的硬件缺陷无关，并指出这与 CPU 接口的处理方式有关。两人都表示将继续跟进此问题，并期待进一步的代码审查。

总体而言，讨论集中在补丁的测试和潜在问题的排查上，双方对解决方案持乐观态度。

#### 📝 邮件列表

1. **[11-09 17:15]** [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-09 17:16]** [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-14 14:20]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when
 interrupts overflow LR capacity
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-14 15:02]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-14 15:53]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when
 interrupts overflow LR capacity
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-14 17:41]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-17 08:22]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when
 interrupts overflow LR capacity
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-17 11:56]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH] KVM: selftests: Add SYNC after guest ITS setup in vgic_lpi_stress

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 15:39:02 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 自测的两个补丁，主要集中在虚拟化环境中 GIC（通用中断控制器）的设置和同步问题。

**原始补丁内容**：
Maximilian Dittgen 提出了一个补丁，目的是在 vgic_lpi_stress 测试中，在进行 GIC 设置后添加 SYNC 命令，以确保 ITS（中断转发系统）在注入 LPIs（本地中断）之前完成映射命令的处理。这样可以避免在 ITS 尚未完成映射时就向虚拟机注入中断，从而导致中断无法正确传递。

**之前讨论要点**：
在历史讨论中，补丁的背景被详细阐述，强调了在进行中断映射时缺乏同步机制可能导致的问题。KVM 理论上并不能保证 ITS 会在注入 LPIs 之前完成映射，尽管在实践中通常是同步处理的。

**本周新讨论与进展**：
本周，Dittgen 提出了两个补丁的更新版本。第一个补丁增加了对 GICR_TYPER.Processor_Number 的断言，以确保其与自测 CPU 索引一致。第二个补丁则实现了在 ITS 映射后添加 SYNC 命令的功能，确保映射完成后再进行中断注入。Oliver Upton 对第一个补丁进行了小幅清理，并建议将补丁的新版本作为单独线程发布，以便于跟踪。两个补丁均已被应用到下一个开发版本中。

#### 📝 邮件列表

1. **[11-14 15:39]** [PATCH] KVM: selftests: Add SYNC after guest ITS setup in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[11-19 14:57]** [PATCH v2 1/2] KVM: selftests: Assert GICR_TYPER.Processor_Number matches selftest CPU number
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
3. **[11-19 14:57]** [PATCH v2 2/2] KVM: selftests: SYNC after guest ITS setup in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
4. **[11-19 14:35]** Re: [PATCH v2 1/2] KVM: selftests: Assert GICR_TYPER.Processor_Number matches selftest CPU number
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 16: [PATCH v3 0/3] KVM ARM64 pre_fault_memory

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 19 Nov 2025 15:49:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM ARM64 的预故障内存（KVM_PRE_FAULT_MEMORY）功能的补丁系列（PATCH v3 0/3）。该功能之前仅在 x86 上可用，旨在减少执行过程中的阶段 2 故障，特别是在内存密集型应用的后复制迁移场景中，以降低延迟。

在历史讨论中，补丁的背景是引入 ARM64 对 KVM_PRE_FAULT_MEMORY 的支持。补丁系列包括三个主要部分：第一个补丁实现了 ARM64 的 KVM_PRE_FAULT_MEMORY ioctl，第二个补丁更新了预故障内存测试以支持 ARM64，最后一个补丁扩展了测试以涵盖不同的虚拟机内存后备。

本周的新讨论中，Jack Thomson 提供了补丁的详细实现和更新。补丁的具体内容包括：
1. 实现了 `kvm_arch_vcpu_pre_fault_memory()` 函数，处理阶段 2 故障逻辑。
2. 使预故障内存测试能够在 ARM64 上运行，并支持不同的来宾页面大小。
3. 增加了选项以测试不同的内存后备类型（如匿名、hugetlb），以验证预故障功能在不同内存配置下的表现。

这些补丁的实施将显著提升 ARM64 环境下 KVM 的性能，尤其是在处理内存故障时。

#### 📝 邮件列表

1. **[11-19 15:49]** [PATCH v3 0/3] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[11-19 15:49]** [PATCH v3 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[11-19 15:49]** [PATCH v3 2/3] KVM: selftests: Enable pre_fault_memory_test for arm64
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
4. **[11-19 15:49]** [PATCH v3 3/3] KVM: selftests: Add option for different backing in pre-fault tests
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>

---

### Thread 17: [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 11 Nov 2025 11:37:54 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 Armv8.8 SPE（可扩展性能监控）特性的补丁系列，主要集中在数据源过滤功能的支持上。历史讨论中，James Clark 提出了第10版补丁（共5个补丁），并在更新中提到修正了文档中的一些错误，明确了数据源过滤与数据源之间的区别，并且引用了之前版本的链接。

在本周的新讨论中，Namhyung Kim 询问了该系列补丁的进展，并表示一旦内核部分落地，他可以合并工具部分的补丁（第3、4、5个）。James Clark 随后回应称，SPE 驱动部分之前受到 Peter 对配置变更的确认的阻碍，而现在已经获得了确认，因此 Will 应该能够接手驱动的合并工作。

总结来看，补丁系列的进展顺利，关键的确认已到位，预计将很快推进到合并阶段。

#### 📝 邮件列表

1. **[11-11 11:37]** [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[11-19 17:54]** Re: [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Namhyung Kim <namhyung@kernel.org>
3. **[11-20 09:19]** Re: [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 18: [PATCH v3 1/4] mm/vmalloc: warn on invalid vmalloc gfp flags

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 18 Nov 2025 15:44:48 -0700

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 Linux 内核的补丁（PATCH v3 1/4），旨在对无效的 vmalloc GFP 标志发出警告。该补丁的背景是，开发者在启动 ARM64 盒子上的虚拟机时遇到了警告，提示使用了不合适的内存分配标志（__GFP_HIGHMEM），并建议修正代码。

在之前的讨论中，开发者 Nathan Chancellor 提到，问题出现在 KVM 的内存分配函数 kvm_arch_alloc_vm() 中，建议是否应该去掉对 __GFP_HIGHMEM 的调用。此标志是在 5.16 版本中引入的，目的是为 KVM 分配添加内存控制组（memcg）会计功能。

本周的新讨论中，Nathan 和其他参与者确认了这个问题，并提出可以将内存分配函数更改为 kvzalloc()，以避免使用不必要的高内存标志。Oliver Upton 和 Christoph Hellwig 也表示支持这一修改，指出在 ARM64 架构上使用高内存标志并不合适。

总结而言，本次讨论围绕如何修正内存分配中的标志问题展开，参与者一致认为应去掉不必要的高内存标志，并考虑使用更合适的内存分配函数。

#### 📝 邮件列表

1. **[11-18 15:44]** Re: [PATCH v3 1/4] mm/vmalloc: warn on invalid vmalloc gfp flags
   - 发件人: Nathan Chancellor <nathan@kernel.org>
2. **[11-18 16:54]** Re: [PATCH v3 1/4] mm/vmalloc: warn on invalid vmalloc gfp flags
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-19 06:44]** Re: [PATCH v3 1/4] mm/vmalloc: warn on invalid vmalloc gfp flags
   - 发件人: Christoph Hellwig <hch@lst.de>

---

### Thread 19: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Nov 2025 15:31:22 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）中的一个补丁，具体内容为“在 tdh_vp_init() 函数周围获取 MMU 锁”。该补丁旨在提高虚拟化环境中的内存管理安全性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了修复或优化 KVM 在处理 TDX（Trusted Domain Extensions）时的内存管理问题。Rick Edgecombe 提到补丁已应用于 kvm-x86 的 tdx 分支，并在提交中添加了更详细的注释，以便于理解。

在本周的新讨论中，Sean Christopherson 对于邮件回复的格式提出了建议，表示希望未来的讨论中避免使用“回复”格式，以免影响工作流程。Rick Edgecombe 对此表示歉意，并确认补丁已成功应用。

总体来看，本周的讨论主要集中在补丁的应用和邮件交流的格式上，没有新的技术问题被提出。

#### 📝 邮件列表

1. **[11-18 15:31]** Re: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[11-19 00:01]** Re: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
3. **[11-19 00:02]** Re: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>

---

### Thread 20: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 16 Nov 2025 16:31:04 +0530

#### 🤖 AI 总结

本邮件讨论主题为针对AmpereOne AC04处理器的错误修复补丁（PATCH v4），主要涉及对其错误AC04_CPU_23的解决方案。

在历史讨论中，Jaikiran Pai询问该补丁是否也适用于AmpereOne AC03系统，因其对AC04系统的适用性进行了确认。D Scott Phillips回应称，该问题仅影响AC04系统，AC03并未受到影响。

在本周的新讨论中，Jaikiran Pai感谢D Scott的快速确认，并提到他们正在调查在运行Oracle Linux的AC03虚拟机上出现的内存写入丢失问题，尤其是在高缓存使用时。Jaikiran表示，他们正在尝试通过不同的内核版本（从5.15.x到6.12）来重现该问题，以确定是否已有内核版本解决了此问题。此外，Jaikiran希望能与D Scott保持联系，以便在调查过程中获取建议并分享进展。

总结来说，补丁主要针对AC04的错误修复，历史讨论确认了其适用性，而本周讨论则聚焦于AC03的内存问题调查及相关的技术交流。

#### 📝 邮件列表

1. **[11-16 16:31]** Re: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: Jaikiran Pai <jai.forums2013@gmail.com>
2. **[11-17 09:17]** Re: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
3. **[11-18 07:15]** Re: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: Jaikiran Pai <jai.forums2013@gmail.com>

---

### Thread 21: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 11:11:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FFA_VERSION 错误检查的修复。历史讨论中，Kornel Dulęba 提出了一个补丁，指出根据 DEN0077 FF-A 规范第 13.2 节，当固件不支持请求的版本时，应该返回 FFA_RET_NOT_SUPPORTED(-1)。然而，当前的错误检查逻辑将从 SMC 层获取的无符号长整型返回值与“-1”进行比较，这导致了类型不匹配的问题。

在本周的新讨论中，Marc Zyngier 对补丁提出了质疑，表示他在受保护模式下启动 KVM 时，未遇到任何相关的错误，尽管在这些环境中不应实现 FF-A。他请求澄清触发此问题的具体情况。

总结而言，历史讨论中提出的补丁旨在修复错误检查逻辑，而本周的讨论则集中在对该补丁有效性的质疑上，特别是其在特定环境下的适用性。

#### 📝 邮件列表

1. **[11-14 11:11]** [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: =?utf-8?q?Kornel_Dul=C4=99ba?= <korneld@google.com>
2. **[11-22 11:36]** Re: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Nov 2025 05:24:49 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理 ARM64 架构时，销毁阶段2页表时的调度问题。历史讨论中，Raghavendra Rao Ananta 提出了一个补丁（patch），旨在解决在突然销毁一个完全映射的 128G 虚拟机时，出现的调度警告。该警告表明 CPU 在超过一定时间内未能进行调度，可能导致性能问题。

在之前的讨论中，主要关注了这一警告的原因和影响，强调了在销毁页表时需要适当的调度，以避免长时间的调度延迟。

在本周的新讨论中，Oliver Upton 对该补丁表示感谢，并确认已将其应用到下一步的开发中。补丁包含三个部分，分别是：1) 仅在空表上删除引用；2) 拆分 kvm_pgtable_stage2_destroy() 函数；3) 在销毁阶段2页表时进行必要的重新调度。这些改动旨在提高系统的稳定性和性能。

#### 📝 邮件列表

1. **[11-13 05:24]** [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[11-19 14:35]** Re: [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the stage-2 page-tables
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 23: [PATCH 6.12.y] KVM: arm64: Make all 32bit ID registers fully writable

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 23 Nov 2025 10:39:09 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 32 位 ID 寄存器的可写性问题。Marc Zyngier 提出了一个补丁（patch），旨在使所有 32 位 ID 寄存器完全可写。该补丁的背景是，现有的更新中常常忽略这些寄存器，导致在 GICv3 机器上恢复 GICv2 客户机时出现问题。

在历史讨论中，虽然没有具体的邮件记录，但可以推测，之前的讨论可能集中在如何处理这些寄存器的可写性以及它们对 KVM 的影响。Marc 指出，KVM 本身并不依赖这些寄存器，因此允许虚拟机监控器（VMM）对客户机进行操作。

在本周的新讨论中，Marc 提交了补丁的具体实现，修改了代码以确保所有 32 位 ID 寄存器在客户机为 32 位时完全可写。他强调，这样的设计不会影响 KVM 的正常运行，因为 KVM 主要关注 64 位特性。补丁已经获得了相关人员的审核，并附上了修复的详细信息和代码修改部分。这一补丁的提交标志着对 32 位 ID 寄存器处理的一个重要进展。

#### 📝 邮件列表

1. **[11-23 10:39]** [PATCH 6.12.y] KVM: arm64: Make all 32bit ID registers fully writable
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH v2 0/4] KVM: selftests: Test SET_NESTED_STATE with 48-bit
 L2 on 57-bit L1

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Nov 2025 10:55:37 -0800

#### 🤖 AI 总结

本邮件主题为“[PATCH v2 0/4] KVM: selftests: Test SET_NESTED_STATE with 48-bit L2 on 57-bit L1”，主要讨论了针对 KVM 的自测试补丁。

1. **原始 patch/问题的内容**：此次补丁包含四个部分，旨在测试在57位L1上使用48位L2的嵌套状态（SET_NESTED_STATE）。补丁的主要目标是增强 KVM 的自测试能力，确保在不同位数的虚拟机环境中能够正确处理嵌套状态。

2. **之前的讨论要点**：由于本邮件没有提供历史讨论的内容，因此无法总结之前的讨论要点。

3. **本周的新讨论、进展或结论**：在本周的讨论中，参与者 Sean Christopherson 确认已将该补丁应用于 kvm-x86 自测试中，并感谢了补丁的提交者 Jim Mattson。补丁的四个部分已分别提交至 GitHub，涵盖了创建和遍历来宾页表的循环使用、修改 VM_MODE 的定义，以及为 LA57 嵌套状态添加 VMX 测试等内容。

总体来看，该补丁的应用将有助于提升 KVM 的稳定性和功能性，特别是在处理不同位数的嵌套状态时。

#### 📝 邮件列表

1. **[11-21 10:55]** Re: [PATCH v2 0/4] KVM: selftests: Test SET_NESTED_STATE with 48-bit
 L2 on 57-bit L1
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 25: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 19 Nov 2025 13:31:26 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（PATCH v5 09/44），其目的是在虚拟机（guest）加载和卸载上下文时，切换 LVTPC（本地向量定时器控制器）到/从中介的 PMI（性能监控中断）向量。

在本周的讨论中，Sean Christopherson 指出该补丁存在问题，因为 `perf_load_guest_context()` 函数并不能保证 `PERF_GLOBAL_CTRL` 的值为 '0'，它仅确保所有事件被禁用。如果没有性能事件，`perf_load_guest_context()` 实际上不会执行任何操作。此外，虽然期望在没有性能事件时 `PERF_GLOBAL_CTRL` 为 '0' 是合理的，但目前的实现并不支持这一点。

他建议在加载客体上下文时，显式清除 `PERF_GLOBAL_CTRL`，因为仅禁用个别计数器并不能全局禁用整个性能监控单元（PMU）。在 VMX 模式下，计数器在 VM 进入和退出时会通过原子方式加载 `PERF_GLOBAL_CONTROL`。因此，即使在 SVM 模式下，也应清除 `PERF_GLOBAL_CONTROL`，以减少可能的性能事件干扰，并确保一致的初始状态。

总的来说，本周的讨论集中在补丁的有效性和实现细节上，提出了对当前设计的改进建议。

#### 📝 邮件列表

1. **[11-19 13:31]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 00/13] Introduce per-vCPU vLPI injection control API

**📧 邮件数**: 16 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Nov 2025 15:02:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于引入每个虚拟 CPU (vCPU) 的虚拟本地外部中断 (vLPI) 注入控制 API 的提案。该提案旨在解决当前只能在虚拟机 (VM) 层面启用 vLPI 直接注入的问题，这种方式在 vCPU 数量超过可用虚拟处理单元 (vPE) 时会导致性能下降。

**原始 Patch/问题内容**：
提案的核心是引入三个新的 ioctl 操作，允许用户空间在运行时动态启用或禁用每个 vCPU 的 vLPI 注入能力。这将提高 I/O 性能，尤其是在 CPU 过度承诺的情况下。

**之前讨论要点**：
历史讨论中提到，当前的 vLPI 注入机制存在资源浪费和性能下降的问题，尤其是在多租户环境中，早期启动的 VM 会占用所有 vPEIDs，导致后续 VM 无法使用直接注入，从而影响性能。

**本周新讨论、进展或结论**：
本周的讨论集中在多个补丁的实现上，包括：
1. 实现了 vLPI 的启用、禁用和查询 ioctl 操作。
2. 解决了 vCPU 调度与 vLPI 启用之间的竞争条件。
3. 添加了自测试以验证 vLPI 控制 API 的正确性。
4. 引入了一个新的 ioctl，用于设置用户空间注入的 MSI 作为软件绕过的 vLPI。

此外，Marc Zyngier 对提案提出了强烈反对，指出在 vCPU 没有启用直接注入的情况下，改变 vLPI 的亲和性会导致中断丢失，这在设计上是不可接受的。他对提案的可行性表示质疑，并要求更清晰的解释。

#### 📝 邮件列表

1. **[11-20 15:02]** [RFC PATCH 00/13] Introduce per-vCPU vLPI injection control API
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[11-20 15:02]** [RFC PATCH 01/13] KVM: Introduce config option for per-vCPU vLPI enablement
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
3. **[11-20 15:02]** [RFC PATCH 02/13] KVM: arm64: Disable auto vCPU vPE assignment with per-vCPU vLPI config
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
4. **[11-20 15:02]** [RFC PATCH 03/13] KVM: arm64: Refactor out locked section of kvm_vgic_v4_set_forwarding()
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
5. **[11-20 15:02]** [RFC PATCH 04/13] KVM: arm64: Implement vLPI QUERY ioctl for per-vCPU vLPI injection API
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
6. **[11-20 15:02]** [RFC PATCH 05/13] KVM: arm64: Implement vLPI ENABLE ioctl for per-vCPU vLPI injection API
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
7. **[11-20 15:02]** [RFC PATCH 06/13] KVM: arm64: Resolve race between vCPU scheduling and vLPI enablement
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
8. **[11-20 15:02]** [RFC PATCH 07/13] KVM: arm64: Implement vLPI DISABLE ioctl for per-vCPU vLPI Injection API
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
9. **[11-20 15:02]** [RFC PATCH 08/13] KVM: arm64: Make per-vCPU vLPI control ioctls atomic
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
10. **[11-20 15:02]** [RFC PATCH 09/13] KVM: arm64: Couple vSGI enablement with per-vCPU vPE allocation
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
11. **[11-20 15:02]** [RFC PATCH 10/13] KVM: selftests: fix MAPC RDbase target formatting in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
12. **[11-20 15:03]** [RFC PATCH 11/13] KVM: Ioctl to set up userspace-injected MSIs as software-bypassing vLPIs
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
13. **[11-20 15:03]** [RFC PATCH 12/13] KVM: arm64: selftests: Add support for stress testing direct-injected vLPIs
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
14. **[11-20 15:03]** [RFC PATCH 13/13] KVM: arm64: selftests: Add test for per-vCPU vLPI control API
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
15. **[11-20 14:40]** Re: [RFC PATCH 00/13] Introduce per-vCPU vLPI injection control API
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[11-20 16:18]** Re: [RFC PATCH 01/13] KVM: Introduce config option for per-vCPU vLPI enablement
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fix for 6.18, take #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 11:34:15 +0000

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.18 版本中的修复补丁。历史讨论中，Marc Zyngier 提出了一个补丁，旨在解决几个回归问题，其中包括一个特别令人烦恼的 FGT 问题。他表示希望这是本周期的最后一个补丁，但对是否真的结束持保留态度。

在本周的新讨论中，Paolo Bonzini 对 Marc 提出的补丁进行了确认，并表示已经将其合并。这表明该补丁得到了认可，并成功纳入了代码库中。

总结来说，此次讨论主要集中在 KVM/arm64 的修复补丁上，Marc Zyngier 提出了补丁并进行了背景说明，而 Paolo Bonzini 则确认了补丁的合并，标志着该问题的解决进展。

#### 📝 邮件列表

1. **[11-14 11:34]** [GIT PULL] KVM/arm64 fix for 6.18, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-18 17:38]** Re: [GIT PULL] KVM/arm64 fix for 6.18, take #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 10:25:45 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于改进 KVM 单元测试中叶函数的回溯信息的补丁（PATCH v2 0/4）。该补丁主要包括四个部分，其中两个关键补丁涉及 x86 和 arm64 的叶函数回溯改进。

在历史讨论中，Mathias Krause 提到补丁已应用于 kvm-x86 的下一个版本，并感谢 Sean Christopherson 的帮助。补丁的目标是提供更好的回溯信息，以便在调试时更容易追踪函数调用。

在本周的新讨论中，Sean Christopherson 指出 x86 的改动导致 realmode 测试失败，决定暂时放弃该改动以不影响其他已应用的补丁。Mathias Krause 进一步分析了问题，发现是由于 GCC 在生成 16 位代码时的一个缺陷，导致寄存器状态的混乱，进而影响了多个 CPU 同时运行的测试。经过深入调查，Krause 发现问题的根本原因在于共享的寄存器状态（'regs'）在多个虚拟 CPU 之间的并发使用，导致寄存器值被错误覆盖。

Krause 提出将 'regs' 变为每个 CPU 独立的解决方案，但认为这需要较大的代码改动，并希望找到更合适的解决方案。最终，他计划提交一个修复补丁以解决这一问题。

#### 📝 邮件列表

1. **[11-14 10:25]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[11-15 05:56]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
3. **[11-17 14:19]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[11-18 02:33]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
5. **[11-18 02:47]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
6. **[11-18 05:04]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
7. **[11-18 12:56]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
8. **[11-18 13:10]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
9. **[11-21 17:44]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>

---

### Thread 2: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 19 Nov 2025 13:18:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于针对 arm64 架构的 KVM 单元测试（kvm-unit-tests）系列补丁（PATCH v3 00/10），主要目的是增加对 EL2 的支持。

在历史讨论中，邮件没有提供具体的背景信息，但可以推测该补丁系列旨在解决当前 KVM 单元测试中缺乏对 EL2 的支持问题，以便更好地进行虚拟化测试。

本周的新讨论中，参与者们对该补丁系列的合并表示关注。Joey Gouly 提到希望能尽快合并该系列补丁，并询问是否有其他人对其进行过测试。Nadav Amit 提出疑问，询问 kvm-unit-tests 是否能够在裸金属的 arm64 硬件上运行，并提到他曾在内部测试中修复过多个问题。Joey 回复称他主要是在 QEMU 环境中进行测试，而 Andrew Jones 则回忆起之前 arm64 构建在裸金属上工作过的情况，并希望有更多对 arm64 感兴趣的开发者参与审查和测试。最后，Marc Zyngier 表示对该补丁的初步审查没有发现问题，并给予了支持。

总体来看，本周的讨论集中在对补丁的测试和审查上，参与者们希望能推动该补丁的合并进程。

#### 📝 邮件列表

1. **[11-19 13:18]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[11-19 15:48]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Nadav Amit <nadav.amit@gmail.com>
3. **[11-19 14:02]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[11-19 09:34]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Andrew Jones <ajones@ventanamicro.com>
5. **[11-19 15:34]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

