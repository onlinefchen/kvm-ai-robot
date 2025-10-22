# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 11:03:50

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 323
- **总 Thread 数**: 54
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 49 threads (308 邮件)
- **RFC**: 2 threads (4 邮件)
- **Bug Report**: 1 threads (2 邮件)
- **GIT PULL**: 1 threads (3 邮件)
- **Other**: 1 threads (6 邮件)

---

## 📌 PATCH

共 49 个 thread

---

### Thread 1: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot

**📧 邮件数**: 35 | **👥 参与者**: 6 | **📅 开始时间**: Tue, 9 Sep 2025 14:46:42 +0100

#### 🤖 AI 总结

本邮件列表讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的内存捐赠功能的补丁（PATCH v4 01/28）。该补丁的目的是添加一个新函数，以便在捐赠内存时能够指定权限。

在历史讨论中，参与者对补丁的实现提出了多个问题和建议，主要集中在权限检查和内存类型的处理上。例如，Will Deacon 提出应该确保捐赠的内存权限为读写（KVM_PGTABLE_PROT_RW），而不是允许其他权限类型的内存捐赠。此外，讨论中还提到需要验证捐赠的内存是否被正确映射，以及如何处理 MMIO（内存映射输入输出）页面的捐赠。

在本周的新讨论中，Mostafa Saleh 对补丁进行了更新，表示将根据 Will 的建议加强权限检查，以确保未来的实现不会出现安全隐患。此外，参与者们还讨论了如何处理 SMMU（系统内存管理单元）驱动中的缓存一致性问题，Jason Gunthorpe 提出应确保 SMMU 驱动在处理共享数据结构时使用可缓存内存，以提高性能。

总体而言，本周的讨论集中在对补丁的细节完善和对未来可能出现的问题进行预防，确保 KVM 在 arm64 架构下的内存管理更加安全和高效。

#### 📝 邮件列表

1. **[09-09 14:46]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 15:12]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-09 15:16]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-09 15:23]** Re: [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-09 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>
6. **[09-09 16:56]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-09 11:30]** Re: [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp SMMUv3
   - 发件人: Daniel Mentz <danielmentz@google.com>
8. **[09-12 14:52]** Re: [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Will Deacon <will@kernel.org>
9. **[09-12 15:18]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
10. **[09-14 19:23]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Pranjal Shrivastava <praan@google.com>
11. **[09-14 20:41]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Pranjal Shrivastava <praan@google.com>
12. **[09-15 11:10]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Pranjal Shrivastava <praan@google.com>
13. **[09-15 14:37]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Pranjal Shrivastava <praan@google.com>
14. **[09-15 13:38]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
15. **[09-15 13:45]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
16. **[09-16 11:56]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[09-16 11:58]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[09-16 13:27]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[09-16 13:43]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[09-16 14:04]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[09-16 14:07]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[09-16 14:09]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[09-16 14:10]** Re: [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[09-16 14:24]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[09-16 14:30]** Re: [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[09-16 14:35]** Re: [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp
 SMMUv3
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[09-16 14:50]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[09-16 15:19]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
29. **[09-17 09:36]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
30. **[09-17 16:01]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
31. **[09-17 12:16]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
32. **[09-17 16:25]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
33. **[09-17 12:59]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
34. **[09-18 11:26]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
35. **[09-18 11:36]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 2: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW

**📧 邮件数**: 27 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 12:44:35 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 S1 页表走查（PTW）和 52 位物理地址（PA）支持的改进。Marc Zyngier 提出了一个包含 16 个补丁的系列，旨在增强 KVM 对 SEA（Synchronous Exception Abort）和 TTW（Translation Table Walk）报告的支持。

**原始补丁内容**：
补丁系列的核心在于实现对 S1PTW 中 SEA 的级别报告，解决了在 S1PTW 故障时未能报告走查级别的问题。补丁还扩展了对 52 位 PA 的支持，使得 KVM 能够处理更大的地址空间。

**之前讨论要点**：
在历史讨论中，Marc 提到当前的实现仅支持 48 位地址，且在处理 52 位 PA 时存在复杂性。补丁系列的目标是通过引入新的过滤机制和改进页表走查逻辑来解决这些问题。

**本周新讨论及进展**：
本周的讨论集中在补丁的具体实现和细节上，Marc 提出了多个补丁的具体功能，包括计算 52 位 TTBR 地址、调整最大输出地址的计算、解耦输出地址与描述符等。Oliver Upton 对部分实现提出了建议和改进意见，最终 Marc 确认了补丁的应用，并表示将其纳入下一个版本中。这些补丁的成功应用将显著提升 KVM 在处理复杂地址映射时的能力，特别是在支持更高物理地址的场景中。

#### 📝 邮件列表

1. **[09-15 12:44]** [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-15 12:44]** [PATCH v2 01/16] KVM: arm64: Add helper computing the state of 52bit PA support
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-15 12:44]** [PATCH v2 02/16] KVM: arm64: Account for 52bit when computing maximum OA
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-15 12:44]** [PATCH v2 03/16] KVM: arm64: Compute 52bit TTBR address and alignment
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-15 12:44]** [PATCH v2 04/16] KVM: arm64: Decouple output address from the PT descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-15 12:44]** [PATCH v2 05/16] KVM: arm64: Pass the walk_info structure to compute_par_s1()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-15 12:44]** [PATCH v2 06/16] KVM: arm64: Compute shareability for LPA2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-15 12:44]** [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit addresses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-15 12:44]** [PATCH v2 08/16] KVM: arm64: Expand valid block mappings to FEAT_LPA/LPA2 support
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-15 12:44]** [PATCH v2 09/16] KVM: arm64: Report faults from S1 walk setup at the expected start level
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[09-15 12:44]** [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[09-15 12:44]** [PATCH v2 11/16] KVM: arm64: Allow EL1 control registers to be accessed from the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[09-15 12:44]** [PATCH v2 12/16] KVM: arm64: Don't switch MMU on translation from non-NV context
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[09-15 12:44]** [PATCH v2 13/16] KVM: arm64: Add filtering hook to S1 page table walk
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[09-15 12:44]** [PATCH v2 14/16] KVM: arm64: Add S1 IPA to page table level walker
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[09-15 12:44]** [PATCH v2 15/16] KVM: arm64: Populate level on S1PTW SEA injection
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[09-15 12:44]** [PATCH v2 16/16] KVM: arm64: selftest: Expand external_aborts test to look for TTW levels
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[09-19 14:58]** Re: [PATCH v2 06/16] KVM: arm64: Compute shareability for LPA2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[09-19 15:00]** Re: [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit
 addresses
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[09-19 15:27]** Re: [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[09-19 15:31]** Re: [PATCH v2 14/16] KVM: arm64: Add S1 IPA to page table level
 walker
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[09-19 15:36]** Re: [PATCH v2 16/16] KVM: arm64: selftest: Expand external_aborts
 test to look for TTW levels
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[09-19 15:37]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA
 in S1 PTW
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[09-20 10:24]** Re: [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[09-20 10:27]** Re: [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit addresses
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[09-21 11:57]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[09-21 12:00]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 24 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 11 Sep 2025 16:49:21 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM 架构下添加 KVM PSCI 版本的 vcpu 属性的补丁（PATCH 0/2）。该补丁旨在允许用户指定特定的 PSCI 版本，以便在 KVM 中通过 KVM_REG_ARM_PSCI_VERSION 寄存器进行请求。历史讨论中，Sebastian Ott 提出了该补丁，并解释了支持不同 PSCI 版本的必要性，尤其是在主机内核版本不同的情况下进行迁移时，可能会导致迁移失败的问题。

在之前的讨论中，Peter Maydell 询问了该补丁的用例，并指出在源和目标主机内核之间的 PSCI 版本不一致时，迁移可能会失败。Sebastian 进一步解释了该补丁的设计思路，旨在提供向后兼容性，避免因 PSCI 版本不匹配而导致的迁移错误。

在本周的新讨论中，Eric Auger 对补丁的默认 PSCI 版本提出了疑问，并建议在补丁中进行一些修改以提高兼容性。Oliver Upton 则提交了与 KVM ARM64 相关的其他补丁，修复了调试和 SError 注入的问题，并得到了参与者的认可和应用。

总体来看，邮件讨论围绕着如何在 KVM 中有效地管理和兼容不同版本的 PSCI，确保在虚拟化环境中的稳定性和可靠性。

#### 📝 邮件列表

1. **[09-11 16:49]** [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[09-11 16:49]** [PATCH 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[09-11 16:49]** [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[09-11 16:18]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
5. **[09-11 17:59]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
6. **[09-11 17:02]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
7. **[09-11 18:29]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
8. **[09-11 17:32]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
9. **[09-11 18:46]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
10. **[09-17 13:31]** [PATCH 0/2] KVM: arm64: nv: Fixes for handling debug, MDCR_EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-17 13:31]** [PATCH 1/2] KVM: arm64: nv: Trap debug registers when in hyp context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-17 13:31]** [PATCH 2/2] KVM: arm64: nv: Apply guest's MDCR traps in nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-18 16:25]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
14. **[09-18 17:26]** Re: [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
15. **[09-18 17:26]** Re: [PATCH 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Eric Auger <eric.auger@redhat.com>
16. **[09-18 16:49]** Re: [PATCH 0/2] KVM: arm64: nv: Fixes for handling debug, MDCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[09-18 09:46]** [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[09-18 09:46]** [PATCH 1/2] KVM: arm64: nv: Treat AMO as 1 when at EL2 and {E2H,TGE} = {1, 0}
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[09-18 09:46]** [PATCH 2/2] [DO NOT SUBMIT] KVM: arm64: selftests: Test effective value of HCR_EL2.AMO
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[09-19 10:58]** Re: [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[09-19 13:39]** Re: [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[09-20 20:51]** [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[09-20 20:51]** [PATCH 1/2] KVM: arm64: selftests: Remove a duplicate register
 listing in set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[09-20 20:52]** [PATCH 2/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 4: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation

**📧 邮件数**: 21 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 12 Sep 2025 17:44:15 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是对 ARM64 架构下 futex 原子操作的重构，主要围绕一个补丁（PATCH RESEND v7 4/6）进行。该补丁旨在重构 futex 的原子操作，以提高其效率和可读性。

在历史讨论中，参与者对补丁的初步实现表示认可，Catalin Marinas 提出了对函数命名的建议，认为在后续补丁中可能需要调整函数名以保持一致性。

本周的新讨论中，Yeoreum Yun 对补丁进行了进一步的修改，决定保留原始命名，并提出了对 CAS 操作的担忧，认为在某些情况下可能会导致失败。Catalin Marinas 和 Will Deacon 提出了使用 C 语言实现的建议，以减少汇编代码的复杂性，并提高可维护性。讨论中还涉及到对 futex 操作的测试覆盖情况，Yeoreum Yun 表示将会增加测试用例以覆盖所有操作。

最终，Yeoreum Yun 决定在补丁中使用 C 语言实现 cmpxchg 操作，并考虑到字节序的支持，计划重新提交补丁以反映这些更改。整体来看，本周的讨论集中在代码实现的细节和测试覆盖的改进上，显示出对代码质量和性能的重视。

#### 📝 邮件列表

1. **[09-12 17:44]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[09-12 17:53]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-15 11:32]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-15 11:39]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-15 20:40]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[09-15 21:35]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
7. **[09-15 23:34]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-16 08:02]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[09-16 10:15]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[09-16 10:24]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[09-16 11:02]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
12. **[09-16 11:16]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
13. **[09-16 13:47]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
14. **[09-16 13:50]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
15. **[09-16 13:53]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[09-16 14:27]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
17. **[09-16 14:45]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
18. **[09-16 14:58]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
19. **[09-16 15:07]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
20. **[09-16 15:15]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
21. **[09-17 10:32]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 5: [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2

**📧 邮件数**: 19 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 17 Sep 2025 14:20:30 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的自测试（selftests）进行的一系列补丁（patch）更新，主要集中在 VHE（Virtualization Host Extensions）和 EL2（Exception Level 2）环境下的测试。

1. **原始补丁内容**：Oliver Upton 提出了 13 个补丁，旨在将现有的自测试基础设施移植到 VHE EL2 环境中，以便更好地测试未被 KVM 使用的 MMU 相关特性。

2. **历史讨论要点**：之前的讨论主要集中在如何创建和初始化 VGICv3（虚拟通用中断控制器），并确保在 VM 创建过程中正确处理 vCPU 和 VGIC 的顺序。补丁中提到需要在默认情况下为 VM 创建 VGICv3，以满足 EL2 的要求。

3. **本周的新讨论和进展**：本周的讨论中，Oliver 提出了多个补丁，涵盖了 VGICv3 的支持检查、EL2 寄存器的别名处理、默认 vCPU 目标的获取、HCR_EL2 的初始化等。特别是补丁 12 和 13 使得自测试能够在 EL2 下运行，并增加了基本的 EL2 运行测试。参与者 Itaru Kitayama 对部分补丁进行了审查，并提出了对 ioctl 调用的建议，Oliver 也对此进行了回应，强调了对特性标志的细粒度控制。

总的来说，这一系列补丁和讨论旨在增强 KVM 在 ARM64 架构下的自测试能力，特别是在 VHE EL2 环境中的适用性和稳定性。

#### 📝 邮件列表

1. **[09-17 14:20]** [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-17 14:20]** [PATCH 01/13] KVM: arm64: selftests: Provide kvm_arch_vm_post_create() in library code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 14:20]** [PATCH 02/13] KVM: arm64: selftests: Initialize VGICv3 only once
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[09-17 14:20]** [PATCH 03/13] KVM: arm64: selftests: Add helper to check for VGICv3 support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-17 14:20]** [PATCH 04/13] KVM: arm64: selftests: Add unsanitised helpers for VGICv3 creation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-17 14:20]** [PATCH 05/13] KVM: arm64: selftests: Create a VGICv3 for 'default' VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-17 14:20]** [PATCH 06/13] KVM: arm64: selftests: Alias EL1 registers to EL2 counterparts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-17 14:20]** [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting default vCPU target
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-17 14:20]** [PATCH 08/13] KVM: arm64: selftests: Select SMCCC conduit based on current EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-17 14:20]** [PATCH 09/13] KVM: arm64: selftests: Use hyp timer IRQs when test runs at EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-17 14:20]** [PATCH 10/13] KVM: arm64: selftests: Use the vCPU attr for setting nr of PMU counters
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-17 14:20]** [PATCH 11/13] KVM: arm64: selftests: Initialize HCR_EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-17 14:20]** [PATCH 12/13] KVM: arm64: selftests: Enable EL2 by default
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[09-17 14:20]** [PATCH 13/13] KVM: arm64: selftests: Add basic test for running in VHE EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[09-18 06:56]** Re: [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting
 default vCPU target
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
16. **[09-17 15:00]** Re: [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting
 default vCPU target
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[09-18 10:25]** Re: [PATCH 01/13] KVM: arm64: selftests: Provide
 kvm_arch_vm_post_create() in library code
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
18. **[09-18 10:45]** Re: [PATCH 03/13] KVM: arm64: selftests: Add helper to check for
 VGICv3 support
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
19. **[09-18 18:44]** Re: [PATCH 02/13] KVM: arm64: selftests: Initialize VGICv3 only once
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 6: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers

**📧 邮件数**: 15 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 16:13:52 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理未定义寄存器的有效 RES0 行为的补丁系列。

1. **原始补丁内容**：补丁系列的目标是确保当某个特性（如 FEAT_FOO）在虚拟机中不可见时，相关寄存器（如 SCTLR2_EL2）中的控制位被设置为 RES0。补丁通过引入新的结构体 `reg_feat_map_desc` 来描述寄存器与特性之间的依赖关系，从而实现这一功能。

2. **之前讨论要点**：在历史讨论中，Marc Zyngier 提到之前的版本存在一些问题，并根据 Oliver 的反馈进行了修正，确保补丁的提交信息更为清晰，并简化了声明宏。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现上，包括对多个寄存器（如 HCRX_EL2、SCTLR2_EL1、TCR2_EL2 等）进行 RES0 处理的转换。Oliver Upton 对补丁进行了审核并表示通过，Ben Horgan 对 MDCR_EL2 的处理提出了疑问，Marc 随后解释了该行代码的冗余性，并表示将在合并前进行修正。最终，Marc 确认所有补丁已成功应用。

整体来看，本周的讨论围绕补丁的细节实现和代码审查展开，确保了补丁的质量和功能的正确性。

#### 📝 邮件列表

1. **[09-18 16:13]** [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-18 16:13]** [PATCH v2 01/10] KVM: arm64: Remove duplicate FEAT_{SYSREG128,MTE2} descriptions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-18 16:13]** [PATCH v2 02/10] KVM: arm64: Add reg_feat_map_desc to describe full register dependency
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-18 16:13]** [PATCH v2 03/10] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-18 16:13]** [PATCH v2 04/10] KVM: arm64: Enforce absence of FEAT_FGT2 on FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-18 16:13]** [PATCH v2 05/10] KVM: arm64: Enforce absence of FEAT_HCX on HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-18 16:13]** [PATCH v2 06/10] KVM: arm64: Convert HCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-18 16:13]** [PATCH v2 07/10] KVM: arm64: Enforce absence of FEAT_SCTLR2 on SCTLR2_EL{1,2}
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-18 16:14]** [PATCH v2 08/10] KVM: arm64: Enforce absence of FEAT_TCR2 on TCR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-18 16:14]** [PATCH v2 09/10] KVM: arm64: Convert SCTLR_EL1 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[09-18 16:14]** [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[09-19 00:04]** Re: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of
 undefined registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-19 11:53]** Re: [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to
 compute_reg_res0_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[09-19 13:10]** Re: [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[09-19 14:15]** Re: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v8 0/5] support FEAT_LSUI and apply it on futex atomic ops

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 12:08:33 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Armv9.6 的 FEAT_LSUI 特性的补丁集，主要涉及在 futex 原子操作中应用该特性。补丁集包含五个部分，分别是：添加 FEAT_LSUI 的 CPU 特性检测、将 FEAT_LSUI 暴露给虚拟机、为 FEAT_LSUI 添加 Kconfig 配置、重构现有的 futex 原子操作实现，以及支持使用 FEAT_LSUI 的 futex 原子操作。

在历史讨论中，补丁从 v7 到 v8 进行了多次修改，主要包括实现 futex_atomic_eor() 和 futex_atomic_cmpxchg()，并对补丁信息进行了调整。

本周的新讨论中，参与者 Yeoreum Yun 提出了对补丁的具体实现细节的讨论，包括对内存一致性的担忧和对代码的优化建议。Mark Rutland 也对代码的可读性和逻辑进行了反馈，提出了对变量命名和重试机制的改进建议。讨论中涉及到的关键问题包括在高竞争情况下的原子操作的内存一致性，以及如何处理不同字节序下的内存布局。

整体来看，邮件讨论集中在如何有效实现和验证 FEAT_LSUI 特性在 futex 原子操作中的应用，同时确保代码的健壮性和可维护性。

#### 📝 邮件列表

1. **[09-17 12:08]** [PATCH v8 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[09-17 12:08]** [PATCH v8 1/5] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-17 12:08]** [PATCH v8 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-17 12:08]** [PATCH v8 3/5] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-17 12:08]** [PATCH v8 4/5] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[09-17 12:08]** [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-17 13:57]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-17 14:04]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[09-17 14:35]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[09-17 14:42]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[09-17 14:57]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[09-17 15:07]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[09-18 10:11]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 8: [PATCH 0/8] KVM: arm64: Handle effective RES0 behaviour of undefined registers

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 17:58:32 +0100

#### 🤖 AI 总结

本邮件讨论主题为「[PATCH 0/8] KVM: arm64: 处理未定义寄存器的有效 RES0 行为」，主要涉及对 KVM 在 ARM64 架构下的寄存器处理进行改进。

**原始 patch/问题内容**：
该系列补丁旨在确保在特定功能不可见时，相关寄存器的控制位被设置为 RES0。例如，当某个功能（如 FEAT_FOO）不可见时，SCTLR2_EL2 中的相应位（FOO）应被设置为 RES0。补丁还涉及到其他系列的整合，以确保 EL2 和 EL1 在架构上的一致性。

**之前讨论要点**：
历史讨论中并未提供具体的上下文信息，但可以推测，参与者们关注如何在 KVM 中更好地处理寄存器的 RES0 行为，以提高系统的稳定性和兼容性。

**本周的新讨论、进展或结论**：
本周的讨论集中在 Marc Zyngier 提出的八个补丁上，涵盖了多个寄存器的 RES0 处理，包括 HCRX_EL2、SCTLR2_EL1 和 MDCR_EL2 等。Oliver Upton 提出了一些建议，包括补丁的文档化和命名的清晰性，以帮助读者理解代码的结构。Marc Zyngier 对此表示认可，并计划在后续版本中进行调整。此外，Marc 还表示将重新提交补丁系列，确保内容的准确性。整体来看，本周的讨论推动了补丁的细化和完善。

#### 📝 邮件列表

1. **[09-17 17:58]** [PATCH 0/8] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 17:58]** [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-17 17:58]** [PATCH 2/8] KVM: arm64: Enforce absence of FEAT_FGT2 on FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-17 17:58]** [PATCH 3/8] KVM: arm64: Enforce absence of FEAT_HCX on HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-17 17:58]** [PATCH 4/8] KVM: arm64: Convert HCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-17 17:58]** [PATCH 5/8] KVM: arm64: Enforce absence of FEAT_SCTLR2 on SCTLR2_EL{1,2}
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-17 17:58]** [PATCH 6/8] KVM: arm64: Enforce absence of FEAT_TCR2 on TCR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-17 17:58]** [PATCH 7/8] KVM: arm64: Convert SCTLR_EL1 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-17 17:58]** [PATCH 8/8] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-17 23:07]** Re: [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT
 registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-18 10:53]** Re: [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v6 00/11] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 10 | **👥 参与者**: 5 | **📅 开始时间**: Fri, 12 Sep 2025 09:17:29 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对虚拟机内存的直接映射移除支持的补丁（PATCH v6 00/11），该补丁旨在缓解Spectre风格的瞬态执行问题。补丁的核心内容是通过在KVM中引入GUEST_MEMFD_FLAG_NO_DIRECT_MAP标志，允许在准备好虚拟机内存后将其从主机内核的直接映射中移除，从而增强安全性。

在历史讨论中，参与者探讨了补丁的实现细节，特别是如何在释放内存时恢复直接映射条目，以及在不同情况下的内存管理策略。Mike Rapoport对补丁表示认可，并提出了一些小的修改建议。

本周的新讨论中，Hugh Dickins提出了关于free_folio()函数的安全性问题，认为在某些情况下传递address_space映射可能会导致潜在的错误。David Hildenbrand对此表示赞同，并探讨了可能的解决方案。Will Deacon则从arm64架构的角度出发，质疑不进行TLB失效处理的安全性，建议将TLB失效作为架构可选项。此外，Roy Patrick回应了关于准备状态与直接映射移除状态分离的讨论，计划在下一次迭代中改进补丁。

整体来看，讨论围绕补丁的安全性、性能影响及其实现细节展开，参与者积极提出建议和改进方案。

#### 📝 邮件列表

1. **[09-12 09:17]** [PATCH v6 00/11] Direct Map Removal Support for guest_memfd
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
2. **[09-12 09:17]** [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
3. **[09-12 09:17]** [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[09-14 10:44]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
5. **[09-15 23:23]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Hugh Dickins <hughd@google.com>
6. **[09-17 16:52]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: David Hildenbrand <david@redhat.com>
7. **[09-18 21:21]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Will Deacon <will@kernel.org>
8. **[09-19 08:25]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[09-19 08:30]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[09-19 08:44]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>

---

### Thread 10: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 8 Sep 2025 13:01:07 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁，内容为添加对 FEAT_{LS64, LS64_V} 的支持。该补丁旨在增强 ARM64 处理器在特定内存操作中的能力，特别是针对设备内存的原子操作。

在历史讨论中，参与者主要关注如何安全地暴露这些新特性给用户空间。Will Deacon 提出了对用户如何知道何时可以安全使用这些指令的担忧，强调了在不支持的内存区域使用这些指令可能导致的错误。Yicong Yang 和 Jonathan Cameron 也讨论了在不同内存类型下的行为及其对用户空间的影响。

在本周的新讨论中，Yicong Yang 指出，硬件能力（hwcap）仅描述 CPU 的能力，而不涵盖整个系统，用户需要自行确保在支持的内存上使用 LS64 指令。Catalin Marinas 进一步补充，虽然 HWCAP 对用户空间有用，但需要明确如果系统不支持该特性，则不应在 CPU ID 字段中设置。最后，参与者们讨论了是否应该从 hwcap 和 cpuinfo 中去掉该特性的广告，并建议在文档中明确这一点，以避免潜在的错误使用。

总体而言，本周的讨论集中在如何安全地使用新特性以及如何在文档中清晰地传达这些信息。

#### 📝 邮件列表

1. **[09-08 13:01]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 09:48]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[09-11 16:50]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-12 14:47]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
5. **[09-15 16:29]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[09-16 15:56]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[09-17 11:51]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[09-17 12:00]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
9. **[09-17 15:20]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[09-18 17:09]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 11: [PATCH v5 0/6] initialize SCTRL2_ELx

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 15:56:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Linux 内核的一个补丁系列，主要内容是初始化 ARM 架构中的 SCTLR2_ELx 寄存器。该补丁系列（[PATCH v5 0/6]）旨在为 ARMv8.8/ARMv9.3 及更高版本提供对 SCTLR2_ELx 寄存器的初步支持，虽然当前内核并不严格需要修改这些寄存器，但未来的架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要对其进行配置。

在历史讨论中，补丁经历了多个版本的修改，主要集中在合并函数、修复寄存器设置错误以及添加文档说明等方面。

本周的新讨论中，Yeoreum Yun 提出了六个补丁，具体包括：
1. 使 SCTLR2_EL1 可访问；
2. 在启动时初始化 SCTLR2_ELx 寄存器；
3. 在 CPU 挂起和恢复时保存/恢复 SCTLR2_EL1；
4. 在 cpu_soft_restart() 时初始化 SCTLR2_EL1；
5. 将 SCTLR2_EL1 设为每个任务独立；
6. 更新文档以说明 FEAT_SCTLR2 的启动要求。

参与者 Will Deacon 对补丁提出了意见，认为在没有实际使用场景的情况下，不应急于合并这些补丁。Yeoreum Yun 表示感谢并接受了反馈。整体来看，本周的讨论集中在补丁的细节和未来使用的必要性上。

#### 📝 邮件列表

1. **[09-17 15:56]** [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[09-17 15:56]** [PATCH v5 1/6] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-17 15:56]** [PATCH v5 2/6] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-17 15:56]** [PATCH v5 3/6] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-17 15:56]** [PATCH v5 4/6] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[09-17 15:56]** [PATCH v5 5/6] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-17 15:56]** [PATCH v5 6/6] docs: arm64: Document booting requirements for FEAT_SCTLR2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-17 16:28]** Re: [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Will Deacon <will@kernel.org>
9. **[09-17 17:44]** Re: [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 12: [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 18 Sep 2025 20:42:05 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 ARM64 架构的 FEAT_LSFE（大系统浮点扩展）特性的支持，主要涉及两个补丁的提交和讨论。

**原始补丁内容**：
补丁 v4 的目标是为 ARM64 架构添加对 FEAT_LSFE 的支持，该特性从 v9.5 开始是可选的，允许对浮点值进行原子内存操作。补丁中提到，虽然当前内核没有对该特性的直接需求，但希望通过提供硬件能力（hwcap）让用户空间能够发现该特性，并允许 KVM 客户端访问相关的 ID 寄存器字段。

**之前的讨论要点**：
在历史讨论中，补丁经历了多个版本的迭代，主要集中在修复构建依赖和测试结果的准确性上。补丁的变化包括去掉不必要的 cc clobber、更新 hwcap 测试中的指令等。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的实现细节和测试方面。Mark Brown 提出了两个补丁的具体实现，分别是将 FEAT_LSFE 暴露给 KVM 客户端和在自测试中添加对该特性的支持。Oliver Upton 和 Marc Zyngier 对补丁进行了审查并表示支持，确认已将补丁应用到相应的代码库中。最终，补丁得到了批准并已合并到下一个版本中，标志着对 FEAT_LSFE 支持的进一步推进。

#### 📝 邮件列表

1. **[09-18 20:42]** [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-18 20:42]** [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-18 20:42]** [PATCH v4 2/2] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-18 13:57]** Re: [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-18 22:17]** Re: [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[09-19 15:43]** Re: (subset) [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-19 19:38]** Re: [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float Extension)
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 13: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 01 Sep 2025 13:40:29 +0100

#### 🤖 AI 总结

本邮件列表讨论的主题是关于 Armv8.8 SPE 特性的补丁（[PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features）。该补丁旨在支持三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性是独立的，可以单独应用，补丁系列包括对相关系统寄存器的更改以及性能工具的调整。

在历史讨论中，James Clark 提出了补丁的初步版本，并说明了每个特性的实现细节，特别是补丁 7 和 8 需要维护者的确认才能进一步处理。

在本周的新讨论中，Will Deacon 表示已应用前六个补丁，并请求对补丁 7 和 8 进行审查。Leo Yan 也跟进请求 Arm64 虚拟化和性能维护者关注这两个补丁。Marc Zyngier 则确认补丁 7 将直接纳入 KVM 树，并表示已将其应用到下一步中。

总体来看，本周的讨论主要集中在补丁的审查和应用进展上，特别是对 KVM 相关补丁的处理。

#### 📝 邮件列表

1. **[09-01 13:40]** [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[09-01 13:40]** [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
3. **[09-18 17:43]** Re: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-19 10:59]** Re: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[09-19 14:29]** Re: [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-19 15:22]** Re: (subset) [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 12:00:50 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核的补丁（patch），主题为“PMCR_EL0.N 是 RAZ/WI。在 Ubuntu 22.04 LTS 中至少出现构建失败，移除设置函数”。该补丁的目的是解决在 Ubuntu 22.04 LTS 中构建时出现的错误。

在历史讨论中，Marc Zyngier 对补丁的描述表示质疑，认为补丁缺乏明确的修复目标，询问是否是为了修复构建失败或其他语义缺陷。Itaru Kitayama 最终表示将放弃该补丁，但 Marc 继续鼓励他详细说明问题。

本周的新讨论中，Itaru 重新审视了补丁，认为尽管 PMCR_EL0.N 的位字段在写入时被忽略，但为了与其他位字段的处理保持一致，应该保留在 `vpmu_counter_access.c` 文件中的写操作检查。他还提供了构建错误的详细信息，显示在编译过程中出现了与位字段掩码相关的错误。Marc 则询问了具体的编译器版本，以便更好地理解问题。

总体来说，讨论围绕补丁的有效性和构建错误展开，参与者们在寻找解决方案的过程中进行了深入的技术交流。

#### 📝 邮件列表

1. **[09-12 12:00]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-12 20:33]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@gmail.com>
3. **[09-12 13:11]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-16 06:31]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
5. **[09-17 19:44]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-18 13:59]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

### Thread 15: [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 21 Sep 2025 06:22:56 +0530

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的 TCR_EL1 字段宏进行清理和更新，主要由 Anshuman Khandual 提出，包含四个补丁（PATCH V5 0/4）。

**原始问题**：当前 TCR_EL1 字段宏分散在 ARM64 平台代码中，包括 KVM 实现。该补丁旨在通过更新所需的寄存器字段定义并进行必要的替换，来清理这些宏。

**历史讨论要点**：在之前的版本中，补丁经历了多次修改，主要包括将工具头文件和 KVM 更改分开、删除未使用的宏、以及根据最新的 ARM 文档更新 TCR_EL1 寄存器字段。

**本周新讨论与进展**：
1. **补丁 1/4**：替换 TCR_NFD[0|1] 宏为 TCR_EL1_NFD[0|1]，以便后续可以完全删除这些临时宏。
2. **补丁 2/4**：更新 TCR_EL1 寄存器字段以符合最新的 ARM 文档，并删除冗余的 SYS_TCR_EL1 定义。
3. **补丁 3/4**：将所有使用的 TCR_EL1 字段宏替换为工具 sysreg 变体，并从 pgtable-hwdef.h 中删除。
4. **补丁 4/4**：将所有必需的 TCR_XXX 宏移动到 KVM 头文件中，以便在 KVM 中继续使用。

这些补丁的清理工作不会引入功能上的变化，旨在提高代码的整洁性和可维护性。

#### 📝 邮件列表

1. **[09-21 06:22]** [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-21 06:22]** [PATCH V5 1/4] tools: header : arm64: Replace TCR_NFD[0|1] with TCR_EL1_NFD[0|1]
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-21 06:22]** [PATCH V5 2/4] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[09-21 06:22]** [PATCH V5 3/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[09-21 06:23]** [PATCH V5 4/4] KVM: arm64: Move inside all required TCR_XXX macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 16: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 19:00:49 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: 验证 pKVM 内存转换的输入范围”，主要讨论了对 pKVM 内存转换过程中输入范围的验证问题。

**原始 patch 内容**：
该补丁旨在解决当前 pKVM 内存转换中缺乏对主机发起的范围验证的问题，可能导致结束边界溢出并绕过后续检查。补丁通过在每个公共函数中添加 `range_is_valid()` 检查来关闭这一漏洞。

**之前讨论要点**：
在历史讨论中并未提及具体内容，但可以推测该问题在之前的讨论中未被充分重视，导致补丁的提出。

**本周新讨论及进展**：
本周的讨论主要集中在补丁的细节和潜在改进上。参与者 Oliver Upton 对补丁表示认可，并提出了对某些边界情况的考虑。Quentin Perret 则建议将溢出计算纳入辅助函数，以增强安全性。Vincent Donnefort 表示愿意根据反馈重新调整补丁，以确保更好的未来兼容性。

总体来看，本周的讨论积极，参与者们对补丁的有效性表示认可，并提出了改进建议，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[09-18 19:00]** [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-18 14:21]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-19 09:52]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Quentin Perret <qperret@google.com>
4. **[09-19 11:01]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[09-19 11:06]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 17: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Sun,  7 Sep 2025 17:59:58 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于对 arm64 平台的 TCR_EL1 字段宏进行清理的补丁（PATCH V4 0/2）。该补丁的目的是将分散在 arm64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏进行整理，更新所需的寄存器字段定义，并将所有必要的 TCR_XXX 宏从 pgtable-hwdef.h 头文件移至 KVM 头文件（asm/kvm_arm.h），以便在 KVM 中继续使用。这一清理工作不会引入任何功能上的变化。

在历史讨论中，Anshuman Khandual 提出了该补丁，并说明了其目的和背景。邮件中提到的补丁包括两个部分：第一部分是清理 TCR_EL1 字段宏，第二部分是将这些宏替换为工具 sysreg 变体，并从原来的头文件中删除。

在本周的新讨论中，Anshuman Khandual 询问了补丁的进展情况。Will Deacon 提出建议，认为不应将工具补丁与架构补丁混合，并建议将 KVM 相关的更新分开。对此，Anshuman Khandual 表示同意，并计划按照一定的顺序拆分这些更改，包括首先更新 arm64 工具 sysreg，然后更新工具头文件和内核，最后进行 KVM 特定的更新。

#### 📝 邮件列表

1. **[09-07 17:59]** [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-07 18:00]** [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-15 07:54]** Re: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[09-18 13:08]** Re: [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-19 14:52]** Re: [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 3 Sep 2025 21:15:43 +1000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v10 05/43），其目的是在 KVM 初始化时检查 RME（Realm Management Extension）支持。补丁的背景是为了确保在虚拟化环境中，只有在支持 RME 的情况下才进行相关操作。

在历史讨论中，Gavin Shan 提出了几个小的修改建议，包括移除冗余的头文件包含和优化代码注释的位置。他还分享了对补丁的测试结果，表示在不同的组合下启动虚拟机时没有遇到明显的问题。

在本周的新讨论中，Steven Price 针对 Gavin 的建议表示赞同，认为尽管可以省略某些头文件的显式包含，但保留它们有助于代码的可维护性。此外，他也讨论了代码中错误处理路径的注释，认为可以通过调整注释位置来提高代码的可读性。

总体来看，本周的讨论主要集中在代码优化和可读性上，参与者们对补丁的细节进行了深入探讨，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[09-03 21:15]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[09-04 10:46]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[09-15 11:55]** Re: [PATCH v10 02/43] arm64: RME: Handle Granule Protection Faults
 (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[09-15 11:55]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
5. **[09-15 11:55]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 19: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:22:24 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 futex 支持 FEAT_LSUI 的补丁（PATCH）。该补丁旨在增强 futex 操作的效率，特别是在使用新指令集时。

在历史讨论中，参与者们探讨了补丁的实现细节和潜在问题。Will Deacon 提出了对使用 CAS（Compare And Swap）指令的疑虑，认为在某些情况下可能更适合使用 exclusives 指令。Catalin Marinas 则建议去掉不必要的 uaccess_ttbr0_*() 函数，认为在支持 LSUI 的硬件上，这些函数是多余的，并对补丁表示了认可。

在本周的新讨论中，Yeoreum Yun 对 Catalin 的建议表示感谢，并表示将进行相应的修改。此外，他还提到，尽管使用 LSUI 进行 cmpxchg 和 eor 操作，但仍将保留 llsc 方法，以避免在 32 位操作中可能出现的 futex 原子操作失败的问题。

总体来看，本周的讨论集中在补丁的细节修改和确保 futex 操作的可靠性上，参与者们达成了一致意见，继续推进补丁的完善。

#### 📝 邮件列表

1. **[09-11 16:22]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-12 18:09]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-12 18:16]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-15 09:24]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-15 10:15]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 20: [PATCH v8 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 02 Sep 2025 12:36:03 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM 在 arm64 架构上实现对 SME（Scalable Matrix Extension）支持的补丁（PATCH v8 00/29）。补丁的主要内容包括用户空间 ABI 的设计，特别是 SVE（Scalable Vector Extension）寄存器的向量长度、访问方式，以及对 ZA 和 ZT0 的访问控制。此外，还涉及到细粒度陷阱控制的添加。

在之前的讨论中，Mark Brown 提出了补丁的初步版本，并寻求对用户空间 ABI 和细粒度陷阱控制的反馈。讨论中提到，现有的控制寄存器是按每个虚拟 CPU（vCPU）管理的，而在补丁中将细粒度陷阱控制设计为按虚拟机（VM）管理，这引发了对其一致性和灵活性的质疑。

本周的新讨论中，Marc Zyngier 提出了对补丁的改进建议，认为细粒度陷阱（FGT）控制应该按每个 vCPU 管理，而不是按 VM 管理，并且应将读写操作的控制分开。他指出，当前的设计在处理细粒度陷阱时缺乏灵活性，建议调整为更符合实际需求的方案。Mark Brown 也表示认同，认为将 FGT 控制调整为按 vCPU 管理会更清晰。整体来看，本周的讨论集中在补丁设计的灵活性和一致性上。

#### 📝 邮件列表

1. **[09-02 12:36]** [PATCH v8 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-02 12:36]** [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-19 16:14]** Re: [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-19 16:53]** Re: [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 09:55:05 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在允许用户空间去除 stage-2 TGRAN（翻译粒度）特性。补丁的主要内容是更新了对 NV（Nested Virtualization）启用虚拟机的处理，允许用户在不允许使用传统值的情况下，去除特定的 TGRAN。

在之前的讨论中，补丁的逻辑主要集中在如何处理用户对 TGRAN 的修改请求，确保在 NV 启用的情况下，用户只能请求合法的 TGRAN 值。补丁中引入了一个新的函数 `tgran2_val_allowed`，用于验证用户请求的值是否有效。

本周的新讨论中，Oliver Upton 提出了补丁的细节，并请求将补丁的署名格式进行小修改，以正确标识贡献者。Suzuki K Poulose 对补丁进行了审查，认为其正确性良好，并建议将函数命名更改为更明确的形式。最后，Marc Zyngier 确认已将补丁应用到下一个版本中，表示感谢。

总体来看，本周的讨论主要围绕补丁的细节确认和小的命名建议，补丁已成功应用。

#### 📝 邮件列表

1. **[09-18 09:55]** [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-18 15:55]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2
 TGRANs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-19 09:07]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2
 TGRANs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[09-19 13:39]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 16 Sep 2025 17:11:03 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 在 arm64 架构下处理 EL2 状态的相关函数 `kvm_vcpu_{set,is}_be()` 的问题。Marc Zyngier 提出的补丁旨在让这些函数能够正确处理 SCTLR_EL2，而不仅仅依赖 SCTLR_EL1，从而解决在 PSCI 中评估或设置字节序时的潜在问题。

在之前的讨论中，Marc 指出当前 KVM 只关注 SCTLR_EL1，忽略了 EL2 状态的影响，而 Oliver Upton 对补丁表示认可，认为现有的清理措施已经到位，并给予了审核通过的反馈。

本周的新进展中，Marc Zyngier 确认补丁已被应用，并感谢 Oliver 的反馈。Oliver 也提到，尽管 SCTLR_EL2 存在一些复杂性，但这是他未来需要解决的任务之一。总体来看，本周的讨论主要集中在补丁的审查和确认上，标志着该问题的修复工作向前推进了一步。

#### 📝 邮件列表

1. **[09-16 17:11]** [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-16 22:21]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2
 state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 09:21]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-17 17:42]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 23: [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  9 Sep 2025 13:36:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 pKVM 和 nvhe 中实现内核崩溃时转储故障指令的补丁。最初的补丁由 Mostafa Saleh 提出，包含两个部分：第一个补丁实现了在 nvhe 的内核崩溃时打印指令代码，第二个补丁则扩展了这一功能到 pKVM。补丁的目的是为了在发生崩溃时提供更详细的调试信息，帮助开发者快速定位问题。

在历史讨论中，Mostafa 提到，当前的实现仅在启用了 `CONFIG_NVHE_EL2_DEBUG` 时有效，并且移除了硬编码的参数 `dump_kernel_instr()`。该补丁得到了 Kunwu Chan 的测试和审核。

在本周的新讨论中，Will Deacon 对第一个补丁表示认可，确认已接受（Acked-by）。同时，Marc Zyngier 也表示已将这两个补丁应用到下一个版本中，确认了补丁的提交。这表明该补丁系列得到了积极的反馈，并且即将合并到主线代码中。

#### 📝 邮件列表

1. **[09-09 13:36]** [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-09 13:36]** [PATCH v2 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[09-15 11:54]** Re: [PATCH v2 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-15 13:07]** Re: [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 12 Sep 2025 17:24:11 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于为 arm64 架构添加 LSUI Kconfig 的补丁（patch）。该补丁旨在检测工具链对 LSUI 的支持，历史讨论中提到，binutils 2.45 版本已增加对 LSUI 的支持。参与者 Catalin Marinas 对补丁给予了积极评价，并提出了一些小的修改建议，例如改善主题描述和调整缩进格式，最终表示“已审阅通过”。

在本周的新讨论中，Yeoreum Yun 表示将根据 Catalin 的建议进行修改，并准备重新提交补丁。然而，Will Deacon 提出在 CAS 讨论未结束之前，请不要重新提交补丁。Yeoreum 随后确认将等待 Will 对相关讨论的评论，以便进一步推进补丁的提交。

总体来看，当前讨论主要集中在补丁的细节修改和相关讨论的进展上，尚未达成最终结论。

#### 📝 邮件列表

1. **[09-12 17:24]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[09-15 11:42]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-15 12:32]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-15 12:41]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 25: [PATCH v2] KVM: arm64: Fix NULL pointer access issue

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 02 Sep 2025 11:48:25 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM (Kernel-based Virtual Machine) 在 arm64 架构下的空指针访问问题。历史讨论中，Yingchao Deng 提出了一个补丁（patch），旨在解决在 Linux 启动于 EL1 模式时，由于 KVM 未初始化而导致的空指针解引用问题。具体来说，当 KVM 的 hyp 模式不可用时，per-CPU 基指针未初始化，导致通过 `host_data_ptr()` 访问时出现空指针错误。为此，补丁中增加了对 `is_kvm_arm_initialised()` 的条件检查，以确保 KVM 初始化完成。

在后续的讨论中，Oliver Upton 指出补丁的简短描述过于模糊，建议更清晰地描述功能变化。Marc Zyngier 在本周的讨论中表示将合并此补丁，并对提交日志进行了重写，使其更具可读性。同时，他对辅助函数进行了重构，以提高代码的整洁度。

本周的进展是，补丁已被应用，修复了 KVM 在 arm64 架构下的空指针访问问题，确保了在 KVM 未初始化时，相关的追踪帮助函数能够安全返回，避免了潜在的崩溃。

#### 📝 邮件列表

1. **[09-02 11:48]** [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng <yingchao.deng@oss.qualcomm.com>
2. **[09-04 00:26]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-15 11:41]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-15 11:49]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:28:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的 futex 实现的补丁，旨在对 `__llsc_futex_atomic_set()` 函数进行小幅优化。补丁的主要内容是尝试通过减少一条指令来提升性能。

在历史讨论中，参与者对该补丁的有效性和维护性提出了质疑。Will Deacon 表示对这个优化的价值持怀疑态度，认为增加新的汇编代码并未显著改善可维护性。Yeoreum Yun 也表示虽然这个补丁可能会带来微小的优化，但如果从维护性角度来看并不理想，可以考虑放弃。Catalin Marinas 进一步指出，除非能展示出明显的性能提升，否则建议暂时搁置该补丁。

在本周的新讨论中，Yeoreum Yun 反馈了 Catalin Marinas 的观点，确认补丁的改进效果不明显，因此决定放弃这个补丁。整体来看，经过讨论，参与者一致认为该补丁并不值得保留。

#### 📝 邮件列表

1. **[09-11 16:28]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:19]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-12 17:36]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-15 11:41]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 27: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 17 Sep 2025 14:07:37 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复 `user_mem_abort()` 函数中的页面泄漏问题。

1. **原始补丁内容**：补丁由 Fuad Tabba 提交，主要修复了 `user_mem_abort()` 函数在处理错误时未能释放页面引用的问题。具体来说，该函数在执行过程中通过 `__kvm_faultin_pfn()` 获取了页面引用，但在后续的属性检查中，如果发现映射不匹配，直接返回错误代码，导致未释放相应的页面。补丁通过在返回错误之前存储错误代码并释放未使用的页面来解决这一问题。

2. **之前的讨论要点**：本线程没有历史讨论，所有内容均为本周的新讨论。

3. **本周的新讨论与进展**：在本周的讨论中，Oliver Upton 对补丁进行了审核并表示赞赏，确认了补丁的有效性。Marc Zyngier 随后表示已将该补丁应用到下一个版本中，确认了补丁的提交成功。

综上所述，此次讨论集中在修复 KVM arm64 的一个重要问题上，补丁得到了积极的反馈并已被采纳。

#### 📝 邮件列表

1. **[09-17 14:07]** [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-17 09:23]** Re: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 17:43]** Re: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 28: [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float Extension)

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 16 Sep 2025 22:13:47 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 arm64 架构支持大型系统浮点扩展（FEAT_LSFE）的补丁（PATCH v3 0/3）。该补丁的主要内容包括为 FEAT_LSFE 添加硬件能力（hwcap）标识，以及相应的自测试（kselftest）支持。

在历史讨论中，补丁的第一部分已经被应用到 arm64 的代码库中，具体是将 hwcap 添加到相关功能中，标识符为 FEAT_LSFE。参与者 Mark Brown 表达了对补丁的感谢，并确认了补丁的应用。

在本周的新讨论中，Will Deacon 对补丁的第三部分提出了疑问，指出可能会在没有编译器知晓的情况下损坏 H0 寄存器，并建议使用 STFADD 指令来避免这个问题。此外，他询问了为何需要 "cc" 约束。Mark Brown 进一步回应，表示使用更简单的约束会更合适，并指出在实际应用中，编译器不太可能在生成的指令中使用浮点操作，因此在大多数情况下是安全的。他认为当前的约束处理方式有些过于复杂。

总体来看，本周的讨论集中在补丁的实现细节和潜在问题上，参与者们对补丁的有效性和安全性进行了深入探讨。

#### 📝 邮件列表

1. **[09-16 22:13]** Re: [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float Extension)
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-16 22:16]** Re: [PATCH v3 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-16 22:54]** Re: [PATCH v3 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 29: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 16:09:42 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个补丁（patch），其内容为支持 FEAT_LSUI 并将其应用于 futex 原子操作。该补丁的目的是增强 Linux 内核在处理原子操作时的性能。

在历史讨论中，参与者 Yeoreum Yun 提出在最新的 Arm 架构文档中找不到有关 FEAT_LSUI 的详细信息，询问应该查找哪些资料。Will Deacon 回应称，目前该信息仅在公共 XML 文档中可用，预计年底会发布更新的 Arm 架构文档，但目前的情况并不理想。

在本周的新讨论中，Will Deacon 和 Catalin Marinas 进行了进一步的交流。Catalin 表示，虽然 XML 文档不如正式文档理想，但仍然比没有信息要好。Will 也表示，只要 Catalin 愿意继续协助审查，补丁的讨论和审查过程可以继续进行。

总体来看，补丁的讨论进展顺利，尽管存在一些文档可用性的问题，但参与者们对继续推进审查持积极态度。

#### 📝 邮件列表

1. **[09-11 16:09]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:22]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-15 21:37]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 30: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 15 Sep 2025 16:52:34 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在更新 `sanitise_mte_tags()` 函数中的过时注释。

原始补丁的内容主要是修正 `sanitise_mte_tags()` 函数中的注释，以反映最近的代码更改。具体来说，之前的注释提到在 MTE（Memory Tagging Extension）启用的情况下，VM_SHARED 映射是不被允许的，但随着提交 c911f0d46879 的更新，这一限制已被取消。此外，提交 d77e59a8fccd 解决了多线程初始化时可能导致标签被多次置零的竞争条件，因此也需要更新相关注释。

在本周的新讨论中，Alexandru Elisei 提出了补丁，并详细解释了注释更新的必要性。Steven Price 对补丁进行了审核并表示支持，Marc Zyngier 则确认已将该补丁应用到下一步的开发中。

总结来说，本次讨论集中在更新 KVM arm64 代码中的注释，以确保其准确反映当前实现，且得到了社区成员的认可与支持。

#### 📝 邮件列表

1. **[09-15 16:52]** [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[09-15 17:02]** Re: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Steven Price <steven.price@arm.com>
3. **[09-15 17:53]** Re: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 31: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Sep 2025 16:50:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“检查 pKVM 内存转换的范围参数”。该补丁的主要目的是在 pKVM 内存转换中增加对主机发起的范围参数的验证，以防止可能的溢出问题。

在历史讨论中，补丁的初始版本（v1）未能充分考虑范围检查的边界情况，可能导致有效的范围被错误地判定为无效。参与者 Vincent Donnefort 提出了在每个公共函数中添加 `check_range_args()` 的检查，以确保范围参数的有效性。

在本周的新讨论中，Vincent Donnefort 提交了补丁的第二个版本（v2），其中增加了对页面数量与页面大小乘积溢出的检查，并重命名了检查函数。Marc Zyngier 对补丁提出了进一步的建议，指出范围检查应包括结束边界，以确保在 64 位范围的上限也能正确处理。Marc 强调了这一点对于虚拟地址（VA）尤其重要。

综上所述，本周的讨论集中在补丁的细节改进和边界条件的处理上，显示出对代码安全性和正确性的重视。

#### 📝 邮件列表

1. **[09-19 16:50]** [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-21 12:29]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 32: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 18:55:49 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对HIP10/HIP10C erratum 162200802的补丁（PATCH v2 0/4），该补丁旨在增加对GICD.num_LPIs可写支持，并修复相关错误。

在历史讨论中，Zhou Wang提到该补丁系列的第一步是实现GICD.num_LPIs的可写支持，随后再添加针对错误的补丁。他表示，如果这个补丁系列得到认可，将会准备与QEMU相关的补丁。此外，他还提供了之前版本（v1）的链接，供参与者参考。

在本周的新讨论中，Marc Zyngier对补丁提出了进一步的建议。他认为在处理硬件状态时，应该优先在GIC级别上制定策略，而不是在用户空间暴露相关内容，直到在内核中达成一致的工作方式。这表明在补丁实施之前，仍需进行更深入的讨论和规划，以确保内核的稳定性和兼容性。

#### 📝 邮件列表

1. **[09-01 18:55]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[09-19 16:52]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 33: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 14:22:47 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的非易失性虚拟机（NV VMs）功能限制的补丁（PATCH 00/11）。该补丁旨在将当前支持的功能与实际的功能限制对齐，修正了一些隐藏的功能，使其能够在 NV VMs 中得到支持。

在历史讨论中，Oliver Upton 提到目前对 NV VMs 隐藏了一些实际上可以支持的功能，部分原因是这些功能对 NV 实现没有影响，或是由于未及时更新功能掩码而导致的错误。他提出将掩码反转为拒绝列表的方式，以更明确地表达不支持的功能，并指出了与 FEAT_DoubleLock 相关的一个错误。

在本周的新讨论中，Marc Zyngier 确认了 Oliver 的补丁已被应用，并列出了补丁中包含的具体提交内容。这些提交包括将多个功能暴露给 NV VMs，如 FEAT_DF2、FEAT_RASv1p1、FEAT_ECBHB 等，同时修正了与 TWED 配置相关的错误。

总体来看，讨论的进展表明补丁已经得到认可并成功应用，进一步改善了 KVM 对 NV VMs 的功能支持。

#### 📝 邮件列表

1. **[09-12 14:22]** [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-19 14:15]** Re: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 34: [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 19:46:19 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在使 EL2 特性字段在 ID_AA64MMFR1_EL1 中可被用户空间写入，以便支持不同特性支持的主机之间的虚拟机实时迁移。

在历史讨论中，Jinqian Yang 提出了该补丁，指出虽然 ID_AA64MMFR1_EL1.VH 是 EL2 特性，但在用户空间中仍然保持为不可写状态。这可能导致在 E2H=1 的情况下，用户空间修改 VH 位为 0 时，来宾内核仍在 vEL2 中运行，从而引发不一致性。

在本周的新讨论中，Marc Zyngier 表示已将该补丁应用到下一个版本中，并感谢 Jinqian Yang 的贡献。补丁包括两个部分：第一个是使 ID_AA64MMFR1_EL1 中的 HCX 和 TWED 字段可由用户空间写入，第二个是针对这些字段的自测试。

总结来看，该补丁的实施将增强 KVM 在不同特性支持的主机间的兼容性，并已获得开发者的认可和应用。

#### 📝 邮件列表

1. **[09-11 19:46]** [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
2. **[09-19 14:15]** Re: [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 35: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 14:24:29 -0300

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Armv8.8 SPE（可扩展性能监测）特性的补丁系列，标识为「PATCH v6 00/12」。该补丁旨在增强 Linux 内核中对 Arm 架构的性能监测功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列是基于之前的讨论和版本（如 v8），并且已经在最新的主线内核上进行了验证。

在本周的新讨论中，Arnaldo Carvalho de Melo 提到希望了解何时可以合并与该补丁相关的工具/perf 部分。Leo Yan 随后回应，感谢 Arnaldo 的关注，并提醒大家，James 在几周前已提交了最新的 v8 版本，并确认该版本可以顺利应用于最新的主线内核。Leo 还提到，接下来需要内核维护者的审查，以便进一步推进该补丁的合并。

总体而言，本周的讨论集中在确认补丁的适用性和推进审查流程上，显示出对 Armv8.8 SPE 特性集成的积极进展。

#### 📝 邮件列表

1. **[09-17 14:24]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Arnaldo Carvalho de Melo <acme@kernel.org>
2. **[09-18 09:15]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 36: [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 17 Sep 2025 17:23:08 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 GICv5 主机的支持，特别是允许 ICC_SRE_EL2 访问的补丁。

1. **原始 patch/问题的内容**：补丁 [PATCH 1/5] 旨在允许在 GICv5 主机上访问 ICC_SRE_EL2 寄存器，这是为了增强 KVM 在处理 GICv5 设备时的能力。

2. **之前的讨论要点**：在本次邮件中并未提到具体的历史讨论内容，但可以推测该补丁是对 GICv5 支持的一个重要补充，可能与之前的补丁系列有关。

3. **本周的新讨论、进展或结论**：本周的讨论中，Marc Zyngier 提到他已经将补丁应用到下一个版本中，并感谢 Sascha Bischoff 的贡献。此外，补丁系列中的其他补丁也得到了应用，包括启用 GICv5 主机的嵌套支持和添加 GICv5 Legacy vCPU 接口能力等。这表明该补丁系列的进展顺利，并且正在逐步整合到主线代码中。

#### 📝 邮件列表

1. **[09-17 17:23]** Re: [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 17:42]** Re: [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement and cleanup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 37: [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't support v2 compatibility

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 17:19:35 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，目的是避免在 GICv3 不支持 v2 兼容性的情况下访问 ICC_SRE_EL2 寄存器。补丁的主要内容是，在每次加载/放置 VHE（Virtual Hypervisor Extension）和每次进入/退出 nVHE（Non-Virtual Hypervisor Extension）时，避免不必要的寄存器访问，以减少性能开销。

在之前的讨论中，Marc Zyngier 提到，当前的实现每次都访问 ICC_SRE_EL2，导致在 NV（Non-Virtual）模式下的性能损失，因为该寄存器总是会触发陷阱。随着现代实现逐渐放弃 v2 兼容性，这种开销显得多余。因此，补丁提出通过静态键来替代 GICv5 中的 v2 兼容性检查。

在本周的新讨论中，Marc Zyngier 提交了补丁，并详细说明了补丁的实现细节。Oliver Upton 对该补丁进行了审核并表示支持，确认了补丁的有效性。这表明补丁得到了认可，并可能会被合并到主线代码中。

#### 📝 邮件列表

1. **[09-17 17:19]** [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't support v2 compatibility
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 09:28]** Re: [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't
 support v2 compatibility
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 38: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 16:13:07 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在启动时初始化 arm64 架构的 SCTLR2_ELx 寄存器的补丁（PATCH v4 2/5）。历史讨论中，Dave Martin 指出，简单地使用 `msr_s SYS_SCTLR_\el, \reg` 并不能正常工作，因为 C 预处理器在汇编宏展开时无法正确构造系统寄存器名称。他认为 Yeoreum Yun 提出的代码看起来合理，但仍然可能在某些情况下导致错误。

在本周的新讨论中，Yeoreum Yun 对之前的讨论进行了回复，表示对延迟回复表示歉意，并指出在当前的使用场景中，除了这个宏之外找不到其他用法。他认为对于入口的情况，仅需检查 "el0" 的情况，因此不需要对其进行广泛应用。他决定目前只将此补丁应用于 `set_sctlr2_elx`，并表示如果未来有新的寄存器需要类似的处理，再进行更广泛的应用。

总结来看，补丁的目的是在启动时初始化 SCTLR2_ELx 寄存器，历史讨论中确认了补丁的合理性，而本周的进展则是决定将补丁应用范围缩小至特定的函数。

#### 📝 邮件列表

1. **[09-01 16:13]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
2. **[09-17 15:28]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 39: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 8 Sep 2025 14:25:18 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于对 KVM 工具的补丁（patch）v3 版本，主要涉及对 arm64 架构的嵌套虚拟化支持。该补丁包含六个部分，旨在增强 KVM 工具在 arm64 平台上的虚拟化能力。

在历史讨论中，Will Deacon 提出了对补丁的关注，询问 Andre Przywara 是否计划根据 Alexandru 的反馈进行补充修改。这表明在之前的讨论中，已经有一些未解决的问题和评论需要被考虑。

在本周的新讨论中，Andre Przywara 确认他会对补丁进行重新调整，以回应 Will 的询问。这表明补丁仍在积极开发中，并且开发者正在努力解决之前的反馈。

总体来看，本周的讨论显示出对补丁的持续关注和开发进展，开发者正在积极响应社区的反馈，以完善嵌套虚拟化支持的功能。

#### 📝 邮件列表

1. **[09-08 14:25]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-16 09:51]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 40: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  9 Sep 2025 08:24:27 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁系列，主要目的是在初始虚拟机设置过程中保留 pKVM 虚拟机句柄。

**原始补丁内容**：
Fuad Tabba 提出的补丁（PATCH v4 0/9）旨在修复在非保护模式下创建和销毁多个虚拟机时出现的错误。补丁的最后一项（9/9）修正了 pkvm_init_host_vm() 调用未受到保护模式启用限制的问题，这导致了在非保护模式下的失败。

**之前讨论要点**：
在历史讨论中，补丁的变化主要集中在修复上述错误，并且进行了基于 Linux 6.17-rc5 的重基。补丁系列还包括对 pKVM 相关代码的重命名和注释澄清，以更好地区分 pKVM 模式与保护虚拟机。

**本周新讨论进展**：
在本周的讨论中，Marc Zyngier 确认了补丁已被应用到下一个版本中，并列出了所有补丁的提交信息。这表明该补丁系列已得到认可并进入实施阶段，标志着在 pKVM 处理方面的进一步进展。

#### 📝 邮件列表

1. **[09-09 08:24]** [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-15 10:50]** Re: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 41: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge
 mappings

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 10:13:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下修复针对使用大页映射的非特权虚拟机（np-guests）的调试检查的补丁（patch）。该补丁旨在解决在特定情况下调试信息不准确的问题。

在历史讨论中，参与者 Vincent Donnefort 提到需要更新补丁中的 Fixes 标签，以确保其指向正确的提交（db14091d8f75），因为这是影响功能的关键点。

在本周的新讨论中，Ben Horgan 表达了他对更新 Fixes 标签的支持，并确认他已经在本地调整了相关内容。Marc Zyngier 则表示无需重新发送补丁，表明他对当前进展的认可。

总体来看，本周的讨论主要集中在补丁的细节调整和确认上，参与者之间的沟通顺畅，表明该补丁的修复工作正在有序进行。

#### 📝 邮件列表

1. **[09-15 10:13]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge
 mappings
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[09-15 10:38]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 42: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 18 Sep 2025 17:10:50 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs”，主要讨论了在 KVM 中添加对中介虚拟性能监控单元（vPMUs）的支持。

在历史讨论中，未提及具体的背景信息，因此我们无法提供详细的历史讨论要点。

在本周的新讨论中，参与者 Sean Christopherson 提到已将 KVM 补丁的约四分之一应用于 kvm-x86 misc，原因是完整的补丁已无法在 6.18 版本中及时提交。他特别强调希望能尽快完成“在 kvm_x86_vendor_init() 之前设置 VMCS”的补丁，以确保设置操作的顺序。此外，他还提到了一些与补丁相关的具体提交，包括对 VMCS 配置的设置、PMU 版本检查、快照主机报告的 PMU 能力等。

总体来看，本周的讨论主要集中在补丁的逐步应用及其对后续开发的影响，特别是确保补丁之间的兼容性和正确的操作顺序。

#### 📝 邮件列表

1. **[09-18 17:10]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 43: [PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu
 model

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 18 Sep 2025 15:40:19 +0800

#### 🤖 AI 总结

本邮件主题为“[PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu model”，主要讨论了对 KVM 主机 CPU 模型的定制化改进。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在增强 ARM 架构下 KVM 的 CPU 模型的灵活性和可定制性，以适应不同的虚拟化需求。

本周的新讨论中，参与者 Cornelia Huck 指出补丁中存在一个小问题：在代码中，`prop_name` 的内存未被释放。具体来说，使用 `g_strdup_printf` 分配的内存需要通过 `g_free` 进行释放。Huck 提出了相应的代码修改建议，确保在使用完 `prop_name` 后能够正确释放其内存，以防止内存泄漏。

总结而言，本周的讨论主要集中在补丁的内存管理问题上，强调了代码的健壮性和资源管理的重要性。

#### 📝 邮件列表

1. **[09-18 15:40]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu
 model
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>

---

### Thread 44: [PATCH kvmtool v3 4/6] arm64: add counter offset control

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:17:32 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 工具的补丁，具体内容为“arm64: 添加计数器偏移控制”。该补丁旨在允许用户更灵活地控制计数器的偏移量。

在历史讨论中，虽然没有具体的邮件记录，但可以推测这个补丁的提出是为了改善用户在使用 KVM 工具时的体验，尤其是在处理计数器偏移时的灵活性。

本周的新讨论中，参与者 Andre Przywara 对补丁中的描述提出了意见。他认为，虽然补丁中提到的“默认值为0”在实现上可能不够准确，但从用户的角度来看，其效果是相同的。他指出，拒绝使用“--counter-offset 0”选项，即使它是默认行为，会让用户感到困惑。他建议，如果需要更详细的解释，可以考虑将其添加到文档中。

总的来说，本周的讨论集中在补丁描述的清晰度和用户体验上，强调了文档的重要性以帮助用户理解默认行为。

#### 📝 邮件列表

1. **[09-16 13:17]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 45: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:16:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 工具的补丁，具体内容为在 arm64 架构下增加对维护中断（maintenance IRQ）设置的支持。该补丁属于 v3 版本的第 3/6 项。

在历史讨论中，并没有提供具体的背景信息，邮件列表中仅有本周的新讨论。

本周的讨论主要由 Andre Przywara 提出，他表示支持 Marc 的观点，强调在使用特定功能之前应先检查该功能是否可用，而不是依赖于某些实现细节。Andre 对于之前的实现进行了修正，并确认了补丁的改进方向。邮件中显示出参与者之间的良好沟通和协作，Andre 表达了对建议的认可，并表示已完成相关的修改。

总体来看，本周的讨论集中在补丁的具体实现细节上，参与者们一致同意遵循清晰的检查模式，以确保代码的可靠性和可维护性。

#### 📝 邮件列表

1. **[09-16 13:16]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 46: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:15:33 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 工具中为 arm64 架构添加初步的嵌套虚拟化支持的补丁（patch）。该补丁旨在实现对嵌套虚拟化的支持，以增强 KVM 的功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了回应对嵌套虚拟化支持的需求，尤其是在 arm64 平台上的应用。

在本周的新讨论中，参与者 Andre Przywara 对补丁中的术语提出了看法。他认为使用“nested”这个术语是最直观的，并且与 KVM 命令行选项一致。他还提到，如果将其描述为“EL2/nested virt is not supported”，可能会更好，但同时也意识到这个讨论可能已经进入了“无意义的争论”阶段（bikeshedding）。这表明，尽管补丁的技术实现可能已经完成，但在术语使用上仍存在一些分歧和讨论。

总体而言，本周的讨论主要集中在补丁的命名和描述上，反映出开发者在细节上的关注。

#### 📝 邮件列表

1. **[09-16 13:15]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 47: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:53:15 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 的补丁集（PATCH v11 0/6）。该补丁集包含六个具体的补丁，主要目标是改进 FF-A（Firmware Framework for Arm）在虚拟化环境中的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前的讨论可能涉及 FF-A 的版本兼容性、初始化过程以及对不支持功能的标记等问题。

本周的新讨论中，Marc Zyngier 确认了该补丁集已被应用，并感谢了 Per Larsen 的贡献。具体补丁包括：
1. 修正主机版本降级尝试的返回值。
2. 在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2。
3. 将 FFA_NOTIFICATION_* 调用标记为不支持。
4. 将可选的 FF-A 1.2 接口标记为不支持。
5. 屏蔽对 FFA_FEATURE 调用的响应。
6. 将支持的 FF-A 版本提升至 1.2。

此次讨论表明，补丁集的实施将增强 KVM 在 arm64 架构下的功能，提升虚拟化性能和兼容性。

#### 📝 邮件列表

1. **[09-15 10:53]** Re: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 48: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:52:09 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 ptdump 功能的一个补丁（patch）。该补丁的主要内容是修改 ptdump 的实现，避免在测试页表项（PTE）时同时检查 PTE_VALID 和其他属性。

在历史讨论中，没有提供具体的上下文或之前的讨论内容，因此我们无法得知补丁的背景或相关的技术细节。

在本周的新讨论中，参与者 Marc Zyngier 对补丁进行了确认，并表示已将其应用到下一步的开发中。补丁的提交哈希为 8673e5b22e1e114213d3ca74f415034aed45e528。此次讨论没有提出新的问题或异议，表明补丁得到了认可并将继续推进。

总结来看，本次邮件主要聚焦于 KVM arm64 的 ptdump 补丁的应用，尽管缺乏历史讨论的背景，但本周的进展显示出该补丁已顺利进入后续开发阶段。

#### 📝 邮件列表

1. **[09-15 10:52]** Re: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 49: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:51:16 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings”，主要讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁。该补丁旨在修复在使用巨大映射时对非页面（np）虚拟机的调试检查问题。

在历史讨论中并没有提供具体的背景信息或之前的讨论内容，因此我们无法得知该补丁的详细背景或引发该补丁的具体问题。

在本周的新讨论中，参与者 Marc Zyngier 回复了 Ben Horgan 的邮件，确认该补丁已被应用到下一个版本中，并表示感谢。补丁的提交 ID 为 2ba972bf71cb71d2127ec6c3db1ceb6dd0c73173。

总结而言，本周的进展是该补丁已成功应用，标志着对 KVM arm64 的调试检查问题的修复工作向前迈进了一步。

#### 📝 邮件列表

1. **[09-15 10:51]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 08:36:26 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[RFC PATCH v1 04/38] tsm: 支持从私有内存进行 DMA 分配”。该补丁旨在改进虚拟机环境中对 DMA（直接内存访问）的支持，特别是在没有分配 IOMMU（输入输出内存管理单元）的情况下。

在历史讨论中，参与者探讨了 DMA 分配的机制及其在不同设备（安全与非安全设备）中的应用。补丁的核心内容是如何在没有 Stage1 SMMU 的情况下，使用 DMA-direct 进行 DMA 操作，并对内存属性进行相应的更新。

本周的新讨论中，Mostafa Saleh 提出了一个关于补丁的基本问题，询问在涉及 IOMMU 的情况下，如何影响 DMA 的跳跃（bouncing）。Aneesh Kumar K.V 解释了当前补丁集的工作机制，指出对于非安全设备，流式 DMA 使用 swiotlb（与虚拟机监控器共享的池），而非流式 DMA 则使用 DMA-direct，并通过 dma_set_decrypted() 更新内存属性。Mostafa 对此表示感谢并确认理解。

总体来看，本周讨论进一步澄清了补丁的实现细节和 DMA 操作的影响，推动了对补丁的理解与评估。

#### 📝 邮件列表

1. **[09-15 08:36]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-16 09:45]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
3. **[09-16 08:16]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 2: [RFC RESEND PATCH] arm64: Rename is_midr_in_range_list and add is_midr_subset_of_range_list

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 21:49:29 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中函数命名和功能的改进，具体涉及到 `is_midr_in_range_list` 函数的重命名及新函数 `is_midr_subset_of_range_list` 的添加。

首先，原始的 patch 提出了将 `is_midr_in_range_list` 函数重命名为 `is_any_midr_in_range_list`，以更明确地表示其功能，即检查是否有任何目标实现的 CPU 在给定范围内。同时，增加了 `is_midr_subset_of_range_list` 函数，以便在处理与 Spectre 相关的安全性问题时使用。

在之前的讨论中，参与者指出虚拟机监控器（VMM）需要确保目标实现 CPU 集合的正确性，并强调如果任何目标实现 CPU 受到影响，则所有 CPU 都应被视为受影响。然而，现有的实现逻辑似乎与这一点相悖，导致 VMM 无法准确判断 CPU 是否受到影响。

本周的讨论中，Jia Qingtong 提出了具体的实现细节，并展示了新函数的用法，强调了新函数在处理 Spectre 相关问题时的重要性。这一改动旨在提高代码的可读性和准确性，确保在处理 CPU 错误时的逻辑更加清晰。

#### 📝 邮件列表

1. **[09-15 21:49]** [RFC RESEND PATCH] arm64: Rename is_midr_in_range_list and add is_midr_subset_of_range_list
   - 发件人: Jia Qingtong <jiaqingtong97@gmail.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Sep 2025 07:20:32 -0700

#### 🤖 AI 总结

本邮件线程讨论了在 KVM ARM 虚拟化环境中出现的一个内核错误，具体是 `kvm_s2_put_page` 函数中的 BUG。该问题由 syzbot 报告，涉及到内存管理中的引用计数错误，导致内核在处理页面时崩溃。

在历史讨论中，虽然没有具体的补丁或详细的背景信息，但可以推测该问题与最近在 Linus 的主干中被回退的 S2 引用计数问题有关。syzbot 提供了相关的错误日志和系统配置，以帮助开发者定位问题。

在本周的新讨论中，syzbot 重申了该问题，并附上了详细的错误信息。Marc Zyngier 回复指出，这个 BUG 可能与刚刚在主干中回退的 S2 引用计数问题有关，而该问题目前并不在 kvmarm/next 分支中。这表明开发者正在关注此问题，并可能会在未来的补丁中进行修复。

#### 📝 邮件列表

1. **[09-19 07:20]** [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: syzbot <syzbot+c41f3ddb8299a30a98b5@syzkaller.appspotmail.com>
2. **[09-19 15:26]** Re: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, round #3

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 10 Sep 2025 13:25:08 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.17 版本中的变更，主要由 Oliver Upton 提出。历史讨论中，Oliver 提到这是针对 6.17 的最终修复集，特别指出他撤回了之前针对 RCU 停滞问题的几个修复，因为这些补丁中存在引用计数和使用后释放（UAF）的问题，之前的临时解决方案未能奏效。此外，邮件中提到了一些常见问题的修复，涉及嵌套虚拟化和虚拟通用中断控制器（vgic）。

在本周的新讨论中，Paolo Bonzini 对 Oliver 的邮件进行了回复，表示感谢并提到会在自己的标签中添加关于撤回的说明。Oliver 随后确认了这一点，表示这是他标签中的一个无意遗漏。

总体来看，本周的讨论主要集中在对历史讨论中提到的撤回修复的确认和补充说明上，未涉及新的技术问题或变更。

#### 📝 邮件列表

1. **[09-10 13:25]** [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-17 19:56]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[09-17 12:58]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 23:54:28 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 单元测试的补丁系列，主题为“改善叶子函数的回溯信息”。该补丁的主要目的是增强在 ARM 和 ARM64 架构中对叶子函数的回溯支持，以便更好地调试和定位问题。

补丁的内容包括：
1. 引入“晚期 CFLAGS”概念，以确保在所有其他可选标志评估后再添加特定的编译标志。
2. 针对 x86 架构，补丁通过伪造性能分析来强制生成叶子函数的栈帧，从而改善回溯信息。
3. 对 ARM64 架构，补丁利用 GCC 的支持强制生成栈帧，以避免回溯中缺失帧的问题。
4. 对 ARM 架构，补丁采用 APCS 栈帧布局来解决叶子函数回溯中的问题。

在之前的讨论中，补丁的初步版本未能解决 ARM 和 ARM64 架构的特定问题。本周的进展包括 Mathias Krause 提交了补丁的第二版，并得到了参与者 Andrew Jones 的认可和测试反馈，确认了 ARM 和 ARM64 的修复有效。

总的来说，本周的讨论集中在补丁的具体实现和测试反馈上，显示出对提升调试能力的积极响应。

#### 📝 邮件列表

1. **[09-15 23:54]** [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
2. **[09-15 23:54]** [kvm-unit-tests PATCH v2 1/4] Makefile: Provide a concept of late CFLAGS
   - 发件人: Mathias Krause <minipli@grsecurity.net>
3. **[09-15 23:54]** [kvm-unit-tests PATCH v2 2/4] x86: Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
4. **[09-15 23:54]** [kvm-unit-tests PATCH v2 3/4] arm64: Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
5. **[09-15 23:54]** [kvm-unit-tests PATCH v2 4/4] arm: Fix backtraces involving leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
6. **[09-16 08:04]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

